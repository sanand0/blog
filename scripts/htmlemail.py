#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "python-frontmatter>=1.0.0",
#     "markdown-it-py>=3.0.0",
#     "premailer>=3.10.0",
#     "pygments>=2.17.0",
#     "typer>=0.12.0",
#     "google-auth>=2.0.0",
#     "google-auth-oauthlib>=1.0.0",
#     "google-auth-httplib2>=0.2.0",
#     "google-api-python-client>=2.0.0",
# ]
# ///
"""Convert markdown blog posts to email-friendly HTML."""

import base64
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import frontmatter
from markdown_it import MarkdownIt
from pygments import highlight as pygments_highlight
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound
import typer
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from premailer import transform
from pygments.formatters import HtmlFormatter

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/userinfo.profile",
]


def resolve_links(html: str, base_url: str) -> str:
    """Resolve relative and absolute links to full URLs.

    Args:
        html: HTML content
        base_url: Base URL for resolving links (e.g., https://www.s-anand.net/blog/post-slug/)

    Returns:
        HTML with resolved links
    """
    from urllib.parse import urljoin

    # Replace href attributes
    def replace_href(match):
        url = match.group(1)
        resolved = urljoin(base_url, url)
        return f'href="{resolved}"'

    # Replace src attributes
    def replace_src(match):
        url = match.group(1)
        resolved = urljoin(base_url, url)
        return f'src="{resolved}"'

    html = re.sub(r'href="([^"]+)"', replace_href, html)
    html = re.sub(r'src="([^"]+)"', replace_src, html)

    return html


def replace_youtube_embeds(html: str) -> str:
    """Replace YouTube iframe embeds with clickable thumbnail images.

    Converts iframes to a format like:
    <a href="https://youtu.be/VIDEO_ID">
        <img src="https://i.ytimg.com/vi_webp/VIDEO_ID/sddefault.webp" alt="YouTube video">
    </a>
    """
    # Match YouTube iframe embeds
    youtube_pattern = r'<iframe[^>]*src="(?:https?:)?//(?:www\.)?youtube\.com/embed/([^"?]+)[^"]*"[^>]*>.*?</iframe>'

    def replace_iframe(match):
        video_id = match.group(1)
        return (
            f'<a href="https://youtu.be/{video_id}">'
            f'<img src="https://i.ytimg.com/vi_webp/{video_id}/sddefault.webp" '
            f'alt="YouTube video" style="max-width: 100%; height: auto;">'
            f"</a>"
        )

    return re.sub(youtube_pattern, replace_iframe, html, flags=re.IGNORECASE | re.DOTALL)


def get_html_attr(tag: str, attr: str) -> str | None:
    """Extract an HTML attribute value from a tag fragment."""
    # Support quoted and unquoted attribute values because markdown HTML snippets vary.
    match = re.search(
        rf"\b{re.escape(attr)}\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))",
        tag,
        flags=re.IGNORECASE,
    )
    if match:
        return match.group(1) or match.group(2) or match.group(3)
    return None


def replace_media_embeds(html: str) -> str:
    """Replace video/audio tags with email-friendly fallback links."""

    def first_source(open_tag: str, inner_html: str) -> str | None:
        # Keep author-declared source order: first playable source should be first in markup.
        if src := get_html_attr(open_tag, "src"):
            return src
        for source_tag in re.findall(r"<source\b[^>]*>", inner_html, flags=re.IGNORECASE):
            if src := get_html_attr(source_tag, "src"):
                return src
        return None

    def replace_match(match: re.Match[str]) -> str:
        media_kind = match.group(1).lower()
        open_tag = match.group(2)
        inner_html = match.group(3)

        source = first_source(open_tag, inner_html)
        title = media_kind.capitalize()
        action = "Watch video" if media_kind == "video" else "Listen to audio"
        parts = (
            [f'<p><strong>{title}:</strong> <a href="{source}">{action}</a></p>']
            if source
            else [f"<p><strong>{title}:</strong> Media unavailable in email</p>"]
        )

        caption_links: list[str] = []
        for track_tag in re.findall(r"<track\b[^>]*>", inner_html, flags=re.IGNORECASE):
            # Only include user-facing timed text tracks; skip metadata/chapter tracks.
            kind = (get_html_attr(track_tag, "kind") or "").lower()
            if kind and kind not in {"captions", "subtitles"}:
                continue
            if track_src := get_html_attr(track_tag, "src"):
                # Use neutral link text for email client consistency.
                caption_links.append(f'<a href="{track_src}">Open captions</a>')

        if caption_links:
            parts.append(f"<p><strong>Captions:</strong> {', '.join(caption_links)}</p>")
        return "".join(parts)

    # DOTALL lets us match media tags spanning multiple lines in markdown-authored HTML.
    return re.sub(
        r"<(video|audio)\b([^>]*)>(.*?)</\1>",
        replace_match,
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )


def markdown_to_email_html(markdown_file: Path) -> tuple[str, str]:
    """Convert a markdown file to email-friendly HTML.

    Args:
        markdown_file: Path to the markdown file

    Returns:
        Tuple of (email subject, email HTML body with inlined CSS)
    """
    # Parse frontmatter and content
    post = frontmatter.load(markdown_file)
    content = re.sub(r"\\[ \t]*(\r?\n)", r"\1", post.content)

    def highlight_code(code: str, lang: str | None, _attrs: str) -> str | None:
        if not lang:
            return None
        try:
            lexer = get_lexer_by_name(lang)
        except ClassNotFound:
            return None
        formatter = HtmlFormatter(style="default", nowrap=True)
        return pygments_highlight(code, lexer, formatter)

    md = (
        MarkdownIt(
            "commonmark",
            {
                "html": True,
                "breaks": True,
                "highlight": highlight_code,
            },
        )
        .enable("table")
        .enable("strikethrough")
    )
    html_content = md.render(content)

    # Replace YouTube embeds with image links
    html_content = replace_youtube_embeds(html_content)
    # Replace video/audio embeds with email-friendly fallback links
    html_content = replace_media_embeds(html_content)

    # Extract slug from markdown file path
    # Expected path: posts/YYYY/slug.md
    slug = markdown_file.stem  # Get filename without extension
    base_url = f"https://www.s-anand.net/blog/{slug}/"

    # Resolve relative/absolute links
    html_content = resolve_links(html_content, base_url)

    # Generate Pygments CSS for syntax highlighting
    formatter = HtmlFormatter(style="default")
    pygments_css = formatter.get_style_defs("pre code")

    # Wrap in a basic HTML structure with simple, human-friendly styling
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{post.get("title", "Blog Post")}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                max-width: 600px;
                background-color: #ffffff;
            }}
            h1, h2, h3, h4, h5, h6 {{
                margin-top: 1.5em;
                margin-bottom: 0.5em;
                font-weight: 600;
            }}
            h1 {{ font-size: 2em; }}
            h2 {{ font-size: 1.5em; }}
            h3 {{ font-size: 1.25em; }}
            p {{ margin-bottom: 1em; }}
            a {{ color: #0366d6; text-decoration: underline; }}
            img {{ max-width: 100%; height: auto; margin: 1em 0; }}
            code {{
                padding: 0.2em 0.4em;
                font-size: 90%;
                background-color: #f5f5f5;
                border-radius: 3px;
                font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace;
            }}
            pre {{
                padding: 1em;
                overflow: auto;
                background-color: #f5f5f5;
                border-radius: 3px;
                margin: 1em 0;
            }}
            pre code {{
                padding: 0;
                background-color: transparent;
            }}
            /* Pygments syntax highlighting styles */
            {pygments_css}
            table {{
                border-collapse: collapse;
                margin: 1em 0;
            }}
            table th, table td {{
                padding: 8px 12px;
                border: 1px solid #ddd;
                text-align: left;
            }}
            table th {{
                font-weight: 600;
                background-color: #f5f5f5;
            }}
            blockquote {{
                padding-left: 1em;
                color: #666;
                border-left: 3px solid #ddd;
                margin: 1em 0;
            }}
            hr {{
                border: 0;
                border-top: 1px solid #ddd;
                margin: 2em 0;
            }}
            ul, ol {{ padding-left: 2em; margin: 1em 0; }}
            li {{ margin-bottom: 0.5em; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Use premailer to inline CSS for email compatibility
    email_html = transform(html_template)

    subject = post.get("title", "Blog Post")
    return subject, email_html


def get_credentials(token_path: Path) -> Credentials:
    """Authenticate and return credentials for Google APIs."""
    creds = None
    credentials_path = Path("credentials.json")

    if not credentials_path.exists():
        typer.echo("Error: credentials.json not found in current directory", err=True)
        raise typer.Exit(1)

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json())

    return creds


def format_recipients(recipients: list[str]) -> str:
    """Format recipients for email headers."""
    return ", ".join(recipients)


def send_email(
    gmail_service, people_service, to: list[str], subject: str, html_body: str, cc: list[str]
):
    """Send an email via Gmail API.

    Args:
        gmail_service: Gmail API service object
        people_service: People API service object
        to: Recipient email addresses
        subject: Email subject
        html_body: HTML email body
        cc: CC recipient email addresses
    """
    # Get sender's email address from Gmail profile
    profile = gmail_service.users().getProfile(userId="me").execute()
    email_address = profile["emailAddress"]

    # Get sender's display name from People API
    person = people_service.people().get(resourceName="people/me", personFields="names").execute()

    # Extract display name (fallback to email if not available)
    display_name = email_address
    if "names" in person and person["names"]:
        display_name = person["names"][0].get("displayName", email_address)

    message = MIMEMultipart("alternative")
    message["To"] = format_recipients(to)
    if cc:
        message["Cc"] = format_recipients(cc)
    message["From"] = f'"{display_name}" <{email_address}>'
    message["Subject"] = subject

    # Attach HTML body
    html_part = MIMEText(html_body, "html")
    message.attach(html_part)

    # Encode the message
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    # Send the message
    gmail_service.users().messages().send(userId="me", body={"raw": raw_message}).execute()


def run_tests() -> None:
    """Run minimal inline tests for markdown rendering and options."""
    import tempfile

    def render(md: str) -> tuple[str, str]:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "post.md"
            path.write_text("---\ntitle: Test\n---\n\n" + md)
            subject, html = markdown_to_email_html(path)
            return subject, html

    _subject, html = render("- A\n  - B\n")
    assert "<ul" in html and "<li" in html and "B" in html

    _subject, html = render("```python\nprint('hi')\n```\n")
    assert "print" in html and "<pre" in html and "<code" in html

    _subject, html = render("| A | B |\n| - | - |\n| 1 | 2 |\n")
    assert "<table" in html and "<th" in html and "<td" in html

    _subject, html = render('<div markdown="1">**bold**</div>')
    assert "<div" in html and "**bold**" in html

    _subject, html = render('<iframe src="https://www.youtube.com/embed/abc123"></iframe>')
    assert "youtu.be/abc123" in html and "i.ytimg.com" in html

    _subject, html = render(
        """
<video controls poster="../poster.webp" title="Demo walkthrough">
  <source src="../clip.webm" type="video/webm">
  <source src="../clip.mp4" type="video/mp4">
  <track kind="captions" src="../clip.en.vtt" srclang="en" label="English">
</video>
"""
    )
    assert "<video" not in html
    assert "<strong>Video:</strong>" in html and "Watch video" in html
    assert "https://www.s-anand.net/blog/clip.webm" in html
    assert "<strong>Captions:</strong>" in html
    assert "https://www.s-anand.net/blog/clip.en.vtt" in html

    _subject, html = render(
        """
<audio controls aria-label="Interview recording">
  <source src="../episode.ogg" type="audio/ogg">
  <source src="../episode.mp3" type="audio/mpeg">
  <track kind="subtitles" src="../episode.en.vtt" srclang="en">
</audio>
"""
    )
    assert "<audio" not in html
    assert "<strong>Audio:</strong>" in html and "Listen to audio" in html
    assert "https://www.s-anand.net/blog/episode.ogg" in html
    assert "<strong>Captions:</strong>" in html
    assert "https://www.s-anand.net/blog/episode.en.vtt" in html

    _subject, html = render("[rel](../x)\n\n![img](../i.png)\n")
    assert "https://www.s-anand.net/blog/x/" in html or "https://www.s-anand.net/blog/x" in html
    assert "https://www.s-anand.net/blog/i.png" in html

    _subject, html = render("Line 1\\\nLine 2\n")
    assert "Line 1" in html and "Line 2" in html and "<br" in html

    assert format_recipients(["a@example.com", "b@example.com"]) == "a@example.com, b@example.com"

    typer.echo("✓ Tests passed")


def main(
    markdown_file: Path | None = typer.Argument(None, help="Markdown file path to convert"),
    email: list[str] = typer.Option(
        None, "--email", help="Send email via Gmail API (repeatable option)"
    ),
    cc: list[str] = typer.Option(None, "--cc", help="Copy emails (repeatable)"),
    token: str = typer.Option("token.json", "--token", help="Gmail API token storage path"),
    test: bool = typer.Option(False, "--test", help="Run inline tests and exit"),
):
    """Convert markdown blog posts to email-friendly HTML.

    The title from the frontmatter will be used as the email subject (not included in body).

    Examples:
        # Print HTML to stdout
        uv run scripts/htmlemail.py ./posts/2026/open-sandals.md

        # Send email via Gmail
        uv run scripts/htmlemail.py ./posts/2026/open-sandals.md --email user@example.com
    """
    if test:
        run_tests()
        raise typer.Exit(0)

    if not markdown_file:
        typer.echo("Error: markdown_file is required unless --test is used", err=True)
        raise typer.Exit(1)

    if not markdown_file.exists():
        typer.echo(f"Error: File not found: {markdown_file}", err=True)
        raise typer.Exit(1)

    # Convert to HTML
    subject, html = markdown_to_email_html(markdown_file)

    if email:
        # Send via Gmail API
        typer.echo(f"Sending email to {', '.join(email)}...")
        creds = get_credentials(Path(token))
        gmail_service = build("gmail", "v1", credentials=creds)
        people_service = build("people", "v1", credentials=creds)
        send_email(gmail_service, people_service, email, subject, html, cc or [])
        typer.echo(f"✓ Email sent to {', '.join(email)} with subject: {subject}")
    else:
        # Print to stdout
        typer.echo(html)


if __name__ == "__main__":
    typer.run(main)
