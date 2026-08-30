from pathlib import Path
import re


def test_weekday_labels_match_sunday_first_calendar_rows():
    template = Path(__file__).parents[1] / "layouts/shortcodes/post-calendar.html"
    labels = re.findall(
        r"<div>(.*?)</div>",
        template.read_text().split('<div class="calendar-weekdays">', 1)[1].split(
            '\n      </div>', 1
        )[0],
    )

    assert labels == ["", "M", "", "W", "", "F", ""]
