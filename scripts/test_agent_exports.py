from pathlib import Path
import importlib.util
import json
import re
import sys


SPEC = importlib.util.spec_from_file_location(
    "build_agent_exports", Path(__file__).with_name("build_agent_exports.py")
)
build_agent_exports = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = build_agent_exports
SPEC.loader.exec_module(build_agent_exports)

PUBLIC = Path("public")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_build_agent_exports_writes_tags_json_and_llms_txt(tmp_path):
    public = tmp_path / "public"
    write(
        public / "blog/corpus.jsonl",
        "\n".join(
            [
                json.dumps(
                    {
                        "title": "LLM Eval",
                        "url": "https://www.s-anand.net/blog/llm-eval/",
                        "date": "2026-01-01",
                        "tags": ["llm-evaluation", "llms"],
                    }
                ),
                json.dumps(
                    {
                        "title": "Data",
                        "url": "https://www.s-anand.net/blog/data/",
                        "date": "2026-01-02",
                        "tags": ["data"],
                    }
                ),
            ]
        )
        + "\n",
    )
    write(public / "blog/corpus.schema.json", "{}")
    write(public / "blog/index.xml", "<rss></rss>")
    write(public / "blog/s-anand/index.html", "<html></html>")
    for tag in ["llm-evaluation", "llms", "data"]:
        write(public / f"blog/tag/{tag}/index.html", "<html></html>")
    write(
        tmp_path / "metadata-tags.yml",
        """tags:
  llm-evaluation:
    description: Posts about LLM evaluation.
  llms:
    description: Posts about LLMs.
  data:
    description: Posts about data.
""",
    )

    tags, llms = build_agent_exports.build_agent_exports(
        public_root=public,
        metadata_tags_path=tmp_path / "metadata-tags.yml",
    )

    assert (public / "llms.txt").is_file()
    assert (public / "blog/tags.json").is_file()
    assert {tag["slug"] for tag in tags} == {"llm-evaluation", "llms", "data"}
    assert "[Corpus JSONL](https://www.s-anand.net/blog/corpus.jsonl)" in llms


def ensure_public_exports() -> None:
    build_agent_exports.build_agent_exports(public_root=PUBLIC)


def urls_in_llms() -> list[str]:
    ensure_public_exports()
    text = (PUBLIC / "llms.txt").read_text(encoding="utf-8")
    return sorted(
        {url.rstrip(".,") for url in re.findall(r"https://www\.s-anand\.net/[^\s)>\"]+", text)}
    )


def public_path_for_url(url: str) -> Path:
    if url == "https://www.s-anand.net/llms.txt":
        return PUBLIC / "llms.txt"
    path = url.removeprefix("https://www.s-anand.net/blog/")
    target = PUBLIC / "blog" / path
    return target / "index.html" if url.endswith("/") else target


def test_llms_txt_is_markdown_and_links_resolve():
    ensure_public_exports()
    text = (PUBLIC / "llms.txt").read_text(encoding="utf-8")

    assert text.startswith("# S Anand\n")
    assert "## Core Resources" in text
    for url in urls_in_llms():
        assert public_path_for_url(url).is_file(), url


def test_tags_json_counts_match_tag_pages():
    ensure_public_exports()
    tags = json.loads((PUBLIC / "blog/tags.json").read_text(encoding="utf-8"))["tags"]

    for tag in tags[:50]:
        html = (PUBLIC / f"blog/tag/{tag['slug']}/index.html").read_text(encoding="utf-8")
        assert html.count('class="post-entry tag-entry"') == tag["count"]


def test_llms_tags_corpus_can_list_llm_evaluation_posts():
    ensure_public_exports()
    llms_text = (PUBLIC / "llms.txt").read_text(encoding="utf-8")
    tags_url = re.search(r"https://www\.s-anand\.net/blog/tags\.json", llms_text).group(0)
    corpus_url = re.search(r"https://www\.s-anand\.net/blog/corpus\.jsonl", llms_text).group(0)
    tags_path = public_path_for_url(tags_url)
    corpus_path = public_path_for_url(corpus_url)
    tags = json.loads(tags_path.read_text(encoding="utf-8"))["tags"]
    llm_eval_tags = {
        tag["slug"]
        for tag in tags
        if "llm" in tag["slug"] and "eval" in (tag["slug"] + " " + tag["description"]).lower()
    }
    records = [json.loads(line) for line in corpus_path.read_text(encoding="utf-8").splitlines()]
    posts = [
        (record["title"], record["date"], record["url"])
        for record in records
        if llm_eval_tags.intersection(record.get("tags") or [])
        and "/posts/" in record.get("source_markdown_url", "")
        and record.get("date")
    ]

    assert "llm-evaluation" in llm_eval_tags
    assert posts
    assert all(title and date and url.startswith("https://www.s-anand.net/blog/") for title, date, url in posts)
