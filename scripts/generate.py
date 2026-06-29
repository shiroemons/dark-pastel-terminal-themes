#!/usr/bin/env python3
"""Generate maintained Dark Pastel theme files from the canonical palette."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE_PATH = ROOT / "palette" / "dark-pastel.yaml"


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


def ansi(palette: dict[str, object], group: str, color: str) -> str:
    return palette["ansi"][group][color]  # type: ignore[index]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def generate_warp_or_orca(palette: dict[str, object]) -> str:
    return f"""name: Dark Pastel
accent: '{palette["accent"]}'
background: '{palette["background"]}'
foreground: '{palette["foreground"]}'
details: darker
cursor: '{palette["cursor"]}'
terminal_colors:
  normal:
    black: '{ansi(palette, "normal", "black")}'
    red: '{ansi(palette, "normal", "red")}'
    green: '{ansi(palette, "normal", "green")}'
    yellow: '{ansi(palette, "normal", "yellow")}'
    blue: '{ansi(palette, "normal", "blue")}'
    magenta: '{ansi(palette, "normal", "magenta")}'
    cyan: '{ansi(palette, "normal", "cyan")}'
    white: '{ansi(palette, "normal", "white")}'
  bright:
    black: '{ansi(palette, "bright", "black")}'
    red: '{ansi(palette, "bright", "red")}'
    green: '{ansi(palette, "bright", "green")}'
    yellow: '{ansi(palette, "bright", "yellow")}'
    blue: '{ansi(palette, "bright", "blue")}'
    magenta: '{ansi(palette, "bright", "magenta")}'
    cyan: '{ansi(palette, "bright", "cyan")}'
    white: '{ansi(palette, "bright", "white")}'
"""


def generate_alacritty(palette: dict[str, object]) -> str:
    return f"""# Colors (Dark Pastel)

[colors.bright]
black = '{ansi(palette, "bright", "black")}'
blue = '{ansi(palette, "bright", "blue")}'
cyan = '{ansi(palette, "bright", "cyan")}'
green = '{ansi(palette, "bright", "green")}'
magenta = '{ansi(palette, "bright", "magenta")}'
red = '{ansi(palette, "bright", "red")}'
white = '{ansi(palette, "bright", "white")}'
yellow = '{ansi(palette, "bright", "yellow")}'

[colors.cursor]
cursor = '{palette["cursor"]}'
text = '{palette["cursor_text"]}'

[colors.normal]
black = '{ansi(palette, "normal", "black")}'
blue = '{ansi(palette, "normal", "blue")}'
cyan = '{ansi(palette, "normal", "cyan")}'
green = '{ansi(palette, "normal", "green")}'
magenta = '{ansi(palette, "normal", "magenta")}'
red = '{ansi(palette, "normal", "red")}'
white = '{ansi(palette, "normal", "white")}'
yellow = '{ansi(palette, "normal", "yellow")}'

[colors.primary]
background = '{palette["background"]}'
foreground = '{palette["foreground"]}'

[colors.selection]
background = '{palette["selection"]}'
text = '{palette["selection_text"]}'
"""


def generate_windows_terminal(palette: dict[str, object]) -> str:
    data = {
        "name": "Dark Pastel",
        "black": ansi(palette, "normal", "black"),
        "red": ansi(palette, "normal", "red"),
        "green": ansi(palette, "normal", "green"),
        "yellow": ansi(palette, "normal", "yellow"),
        "blue": ansi(palette, "normal", "blue"),
        "purple": ansi(palette, "normal", "magenta"),
        "cyan": ansi(palette, "normal", "cyan"),
        "white": ansi(palette, "normal", "white"),
        "brightBlack": ansi(palette, "bright", "black"),
        "brightRed": ansi(palette, "bright", "red"),
        "brightGreen": ansi(palette, "bright", "green"),
        "brightYellow": ansi(palette, "bright", "yellow"),
        "brightBlue": ansi(palette, "bright", "blue"),
        "brightPurple": ansi(palette, "bright", "magenta"),
        "brightCyan": ansi(palette, "bright", "cyan"),
        "brightWhite": ansi(palette, "bright", "white"),
        "background": palette["background"],
        "foreground": palette["foreground"],
        "cursorColor": palette["cursor"],
        "selectionBackground": palette["selection"],
    }
    return json.dumps(data, indent=2) + "\n"


def main() -> None:
    palette = load_palette()
    shared_yaml = generate_warp_or_orca(palette)
    write(ROOT / "themes" / "warp" / "Dark Pastel.yaml", shared_yaml)
    write(ROOT / "themes" / "orca" / "Dark Pastel.yaml", shared_yaml)
    write(ROOT / "themes" / "alacritty" / "Dark Pastel.toml", generate_alacritty(palette))
    write(
        ROOT / "themes" / "windowsterminal" / "Dark Pastel.json",
        generate_windows_terminal(palette),
    )


if __name__ == "__main__":
    main()
