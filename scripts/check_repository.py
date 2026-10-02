"""Validate local document links, source coverage and public content guardrails."""
from pathlib import Path
import json
import re
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    errors = []
    files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts]
    forbidden = {".pdf", ".sql", ".zip", ".png", ".jpg", ".jpeg"}
    for p in files:
        if p.suffix.lower() in forbidden:
            errors.append(f"Sensitive/binary artifact requires review: {p.relative_to(root)}")
        text = p.read_text(errors="replace")
        # Expressions avoid embedding the sensitive value in this checker itself.
        patterns = [r"PHPSESS" + r"ID\s*=", r"\$" + r"pdf\$", r"\b\d{13,14}\b", r"mediroza" + r"hospital\.com"]
        for pattern in patterns:
            if re.search(pattern, text, re.I):
                errors.append(f"Possible confidential value: {p.relative_to(root)}")
        if p.suffix == ".md":
            for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
                if link.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = (p.parent / link.split("#")[0]).resolve()
                if not target.is_relative_to(root) or not target.exists():
                    errors.append(f"Broken local link in {p.relative_to(root)}: {link}")
    manifest = json.loads((root / "evidence/source-manifest.json").read_text())
    if manifest["file_count"] != 64 or len(manifest["files"]) != 64:
        errors.append("Source coverage differs from 64 artifacts")
    images = [x for x in manifest["files"] if x["path"].endswith(".png")]
    index = (root / "evidence/EVIDENCE_INDEX.md").read_text()
    if len(images) != 45 or len(re.findall(r"^\| E\d{2} \|", index, re.M)) != 45:
        errors.append("Screenshot evidence coverage differs from 45")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(files)} files; local links; 64 source artifacts; 45 evidence entries; content guardrails.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
