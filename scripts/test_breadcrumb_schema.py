import json
import re
from pathlib import Path


PUBLIC = Path(__file__).parents[1] / "public" / "blog"
JSON_LD = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.DOTALL)


def test_breadcrumb_items_have_names():
    missing = []
    for path in PUBLIC.rglob("index.html"):
        for raw in JSON_LD.findall(path.read_text(encoding="utf-8")):
            data = json.loads(raw)
            if data.get("@type") != "BreadcrumbList":
                continue
            for item in data["itemListElement"]:
                nested = item.get("item")
                name = item.get("name") or (nested.get("name") if isinstance(nested, dict) else None)
                if not name:
                    missing.append(f"{path.relative_to(PUBLIC)} position {item.get('position')}")
    assert not missing, "Breadcrumb items missing names:\n" + "\n".join(missing)
