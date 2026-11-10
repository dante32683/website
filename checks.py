"""Check static portfolio contracts with Python and Node, without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.tags, self.copy, self.scripts = path, [], [], []
        self.script = None
        self.script_type = None
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        self.tags.append((tag, dict(attributes)))
        if tag == "script":
            self.script = []
            self.script_type = dict(attributes).get("type", "text/javascript")

    def handle_endtag(self, tag):
        if tag == "script":
            self.scripts.append((self.script_type, "".join(self.script)))
            self.script = None

    def handle_data(self, text):
        (self.script if self.script is not None else self.copy).append(text)


root = Path(__file__).resolve().parent
pages = {path.resolve(): Page(path) for path in root.rglob("*.html")}
for path, page in pages.items():
    label = path.relative_to(root)
    ids = [attrs["id"] for _, attrs in page.tags if "id" in attrs]
    assert len(ids) == len(set(ids)), f"{label}: duplicate IDs"
    assert any(tag == "img" and attrs.get("class") == "headshot"
               and attrs.get("alt") == "Dante Martin" for tag, attrs in page.tags), f"{label}: missing identity photo"
    assert any(tag == "button" and attrs.get("id") == "theme-toggle"
               and attrs.get("type") == "button" for tag, attrs in page.tags), f"{label}: missing theme button"
    assert any(tag == "div" and attrs.get("class") == "contact"
               for tag, attrs in page.tags), f"{label}: missing contacts"
    assert not re.search(r"\b(?:click|tap) to\b", " ".join(page.copy), re.I), f"{label}: describe the action directly"
    for tag, attrs in page.tags:
        if tag != "a":
            continue
        href = attrs.get("href", "")
        if ":" in href or not href:
            continue
        target, _, fragment = href.partition("#")
        destination = (root / target.lstrip("/") if target.startswith("/") else path.parent / target) if target else path
        if destination.is_dir():
            destination /= "index.html"
        assert destination.exists(), f"{label}: missing link target {href}"
        if fragment:
            target_page = pages[destination.resolve()]
            assert any(a.get("id") == fragment for _, a in target_page.tags), f"{label}: missing anchor {href}"
    for index, (script_type, script) in enumerate(page.scripts):
        # JSON-LD is data, and is not an executable script.
        if script_type == "application/ld+json":
            continue
        result = subprocess.run(["node", "--check"], input=script, text=True, capture_output=True)
        assert result.returncode == 0, f"{label}: inline script {index}: {result.stderr}"
print(f"Passed: {len(pages)} pages, identity controls, copy, local links, anchors, and inline JavaScript.")
