"""Offline comparison of a local source folder to the supplied artifact manifest."""
from pathlib import Path
import argparse
import hashlib
import json
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Local extracted Project folder")
    args = parser.parse_args()
    manifest = json.loads((Path(__file__).resolve().parents[1] / "evidence/source-manifest.json").read_text())
    base = args.source.resolve()
    failures = []
    for item in manifest["files"]:
        path = (base / item["path"]).resolve()
        if not path.is_relative_to(base):
            failures.append("Unsafe manifest path")
        elif not path.is_file():
            failures.append(f"Missing: {item['path']}")
        elif path.stat().st_size != item["size_bytes"] or hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            failures.append(f"Mismatch: {item['path']}")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"Verified {len(manifest['files'])} supplied artifacts locally.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
