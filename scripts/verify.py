#!/usr/bin/env python3
"""Verify Dark Pastel theme files against the canonical palette."""

from __future__ import annotations

import json
import plistlib
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE_PATH = ROOT / "palette" / "dark-pastel.yaml"
THEMES_DIR = ROOT / "themes"
EXPECTED_THEME_COUNT = 38
HEX_RE = re.compile(r"#[0-9a-fA-F]{6}")


def load_palette() -> dict[str, object]:
    palette: dict[str, object] = {"ansi": {"normal": {}, "bright": {}}}
    section: str | None = None
    subsection: str | None = None

    for raw_line in PALETTE_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        stripped = line.strip()
        if not raw_line.startswith(" "):
            key, value = split_yaml_line(stripped)
            if value is None:
                section = key
                subsection = None
            else:
                palette[key] = unquote(value)
                section = None
                subsection = None
        elif raw_line.startswith("  ") and not raw_line.startswith("    "):
            key, value = split_yaml_line(stripped)
            if value is None:
                subsection = key
            elif section:
                palette.setdefault(section, {})[key] = unquote(value)  # type: ignore[index]
        elif raw_line.startswith("    ") and section == "ansi" and subsection:
            key, value = split_yaml_line(stripped)
            if value is None:
                raise ValueError(f"Invalid palette line: {raw_line}")
            palette["ansi"][subsection][key] = unquote(value)  # type: ignore[index]

    return palette


def split_yaml_line(line: str) -> tuple[str, str | None]:
    if ":" not in line:
        raise ValueError(f"Invalid palette line: {line}")
    key, value = line.split(":", 1)
    value = value.strip()
    return key.strip(), value or None


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def expected_colors(palette: dict[str, object]) -> set[str]:
    colors = {
        str(palette["background"]),
        str(palette["foreground"]),
        str(palette["cursor"]),
    }
    for group in ("normal", "bright"):
        colors.update(palette["ansi"][group].values())  # type: ignore[index]
    return {color.lower() for color in colors}


def parse_known_formats(path: Path) -> None:
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8", errors="ignore")
    if suffix == ".json" or suffix == ".termcolors":
        json.loads(text)
    elif suffix == ".toml":
        tomllib.loads(text)
    elif suffix in {".itermcolors", ".terminal"} or text.startswith("<?xml"):
        plistlib.loads(path.read_bytes())


def collect_hex_colors(path: Path) -> set[str]:
    return {match.group(0).lower() for match in HEX_RE.finditer(path.read_text(encoding="utf-8", errors="ignore"))}


def main() -> int:
    failures: list[str] = []
    palette = load_palette()
    expected = expected_colors(palette)
    theme_files = sorted(path for path in THEMES_DIR.glob("*/*") if path.is_file())

    if len(theme_files) != EXPECTED_THEME_COUNT:
        failures.append(f"expected {EXPECTED_THEME_COUNT} theme files, found {len(theme_files)}")

    for path in theme_files:
        rel = path.relative_to(ROOT)
        try:
            parse_known_formats(path)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{rel}: parse failed: {exc}")
            continue

        colors = collect_hex_colors(path)
        if colors:
            missing = expected - colors
            if path.match("*/freebsd_vt/*"):
                # FreeBSD VT maps the normal white slot to #ffffff in the
                # upstream format and cannot represent the full palette one to
                # one.
                missing.discard("#bbbbbb")
            if missing:
                failures.append(f"{rel}: missing canonical colors: {', '.join(sorted(missing))}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print(f"Verified {len(theme_files)} Dark Pastel theme files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
