# dark-pastel-terminal-themes

Dark Pastel theme files for terminals and terminal-adjacent tools.

The canonical palette is based on the `Dark Pastel` scheme from
[mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes).
This repository keeps that palette in one place and stores ready-to-use theme
files for each supported app.

## Palette

The source of truth is [`palette/dark-pastel.yaml`](palette/dark-pastel.yaml).

| Role | Color |
| --- | --- |
| Background | `#000000` |
| Foreground | `#ffffff` |
| Cursor | `#bbbbbb` |
| Selection | `#b5d5ff` |
| Accent | `#ff5e7d` |

ANSI colors:

| Index | Name | Color |
| --- | --- | --- |
| 0 | Black | `#000000` |
| 1 | Red | `#ff5555` |
| 2 | Green | `#55ff55` |
| 3 | Yellow | `#ffff55` |
| 4 | Blue | `#5555ff` |
| 5 | Magenta | `#ff55ff` |
| 6 | Cyan | `#55ffff` |
| 7 | White | `#bbbbbb` |
| 8 | Bright Black | `#555555` |
| 9 | Bright Red | `#ff5555` |
| 10 | Bright Green | `#55ff55` |
| 11 | Bright Yellow | `#ffff55` |
| 12 | Bright Blue | `#5555ff` |
| 13 | Bright Magenta | `#ff55ff` |
| 14 | Bright Cyan | `#55ffff` |
| 15 | Bright White | `#ffffff` |

## Themes

Theme files live under [`themes/`](themes/), grouped by target format.

| Target | File |
| --- | --- |
| Alacritty | `themes/alacritty/Dark Pastel.toml` |
| dynamic-colors | `themes/dynamic-colors/Dark Pastel.sh` |
| Electerm | `themes/electerm/Dark Pastel.txt` |
| Foot | `themes/foot/Dark Pastel.ini` |
| FreeBSD VT | `themes/freebsd_vt/Dark Pastel.conf` |
| Generic shell | `themes/generic/Dark Pastel.sh` |
| Ghostty | `themes/ghostty/Dark Pastel` |
| HexChat | `themes/hexchat/Dark Pastel.conf` |
| iTerm2 dynamic colors | `themes/iterm-dynamic-colors/Dark Pastel.sh` |
| iTerm2 | `themes/schemes/Dark Pastel.itermcolors` |
| Kitty | `themes/kitty/Dark Pastel.conf` |
| Konsole | `themes/konsole/Dark Pastel.colorscheme` |
| LXTerminal | `themes/lxterminal/Dark Pastel.conf` |
| MobaXterm | `themes/mobaxterm/Dark Pastel.ini` |
| Orca | `themes/orca/dark-pastel.yaml` |
| Pantheon Terminal | `themes/pantheonterminal/Dark Pastel.sh` |
| Ptyxis | `themes/ptyxis/Dark Pastel.palette` |
| PuTTY | `themes/putty/Dark Pastel.reg` |
| Remmina | `themes/remmina/Dark Pastel.colors` |
| Rio | `themes/rio/Dark Pastel.toml` |
| Royal TS | `themes/royalts/Dark Pastel.termcolors` |
| TermFrame | `themes/termframe/Dark Pastel.toml` |
| Terminal.app | `themes/terminal/Dark Pastel.terminal` |
| Terminator | `themes/terminator/Dark Pastel.config` |
| Termite | `themes/termite/Dark Pastel` |
| Termux | `themes/termux/Dark Pastel.properties` |
| Tilda | `themes/tilda/Dark Pastel.itermcolors_config_0` |
| VHS | `themes/vhs/Dark Pastel.json` |
| Vim | `themes/vim/Dark-Pastel.vim` |
| VS Code | `themes/vscode/Dark Pastel.json` |
| Warp | `themes/warp/dark-pastel.yaml` |
| Wayst | `themes/wayst/Dark Pastel` |
| WezTerm | `themes/wezterm/Dark Pastel.toml` |
| Windows Terminal | `themes/windowsterminal/Dark Pastel.json` |
| Xfce Terminal | `themes/xfce4terminal/Dark Pastel.theme` |
| Xresources | `themes/Xresources/Dark Pastel` |
| XRDB | `themes/xrdb/Dark Pastel.xrdb` |
| Zed | `themes/zed/dark_pastel.json` |

## Regenerate Maintained Files

Some formats are generated directly from the canonical palette:

```sh
python3 scripts/generate.py
```

Generated files currently include Alacritty, Windows Terminal, Warp, and Orca.
Other upstream formats are kept as imported files because their target apps use
format-specific conventions beyond the shared ANSI palette.

## Verify

Run:

```sh
python3 scripts/verify.py
```

The verifier checks:

- the expected theme file count
- JSON, TOML, and plist syntax for parseable formats
- canonical background, foreground, cursor, and ANSI colors where files use HEX
  color notation

## Sources

- Original Dark Pastel scheme:
  [mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)
