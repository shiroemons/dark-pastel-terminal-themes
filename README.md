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
| Alacritty | [`themes/alacritty/Dark Pastel.toml`](themes/alacritty/Dark%20Pastel.toml) |
| dynamic-colors | [`themes/dynamic-colors/Dark Pastel.sh`](themes/dynamic-colors/Dark%20Pastel.sh) |
| Electerm | [`themes/electerm/Dark Pastel.txt`](themes/electerm/Dark%20Pastel.txt) |
| Foot | [`themes/foot/Dark Pastel.ini`](themes/foot/Dark%20Pastel.ini) |
| FreeBSD VT | [`themes/freebsd_vt/Dark Pastel.conf`](themes/freebsd_vt/Dark%20Pastel.conf) |
| Generic shell | [`themes/generic/Dark Pastel.sh`](themes/generic/Dark%20Pastel.sh) |
| Ghostty | [`themes/ghostty/Dark Pastel`](themes/ghostty/Dark%20Pastel) |
| HexChat | [`themes/hexchat/Dark Pastel.conf`](themes/hexchat/Dark%20Pastel.conf) |
| iTerm2 dynamic colors | [`themes/iterm-dynamic-colors/Dark Pastel.sh`](themes/iterm-dynamic-colors/Dark%20Pastel.sh) |
| iTerm2 | [`themes/schemes/Dark Pastel.itermcolors`](themes/schemes/Dark%20Pastel.itermcolors) |
| Kitty | [`themes/kitty/Dark Pastel.conf`](themes/kitty/Dark%20Pastel.conf) |
| Konsole | [`themes/konsole/Dark Pastel.colorscheme`](themes/konsole/Dark%20Pastel.colorscheme) |
| LXTerminal | [`themes/lxterminal/Dark Pastel.conf`](themes/lxterminal/Dark%20Pastel.conf) |
| MobaXterm | [`themes/mobaxterm/Dark Pastel.ini`](themes/mobaxterm/Dark%20Pastel.ini) |
| Orca | [`themes/orca/Dark Pastel.yaml`](themes/orca/Dark%20Pastel.yaml) |
| Pantheon Terminal | [`themes/pantheonterminal/Dark Pastel.sh`](themes/pantheonterminal/Dark%20Pastel.sh) |
| Ptyxis | [`themes/ptyxis/Dark Pastel.palette`](themes/ptyxis/Dark%20Pastel.palette) |
| PuTTY | [`themes/putty/Dark Pastel.reg`](themes/putty/Dark%20Pastel.reg) |
| Remmina | [`themes/remmina/Dark Pastel.colors`](themes/remmina/Dark%20Pastel.colors) |
| Rio | [`themes/rio/Dark Pastel.toml`](themes/rio/Dark%20Pastel.toml) |
| Royal TS | [`themes/royalts/Dark Pastel.termcolors`](themes/royalts/Dark%20Pastel.termcolors) |
| TermFrame | [`themes/termframe/Dark Pastel.toml`](themes/termframe/Dark%20Pastel.toml) |
| Terminal.app | [`themes/terminal/Dark Pastel.terminal`](themes/terminal/Dark%20Pastel.terminal) |
| Terminator | [`themes/terminator/Dark Pastel.config`](themes/terminator/Dark%20Pastel.config) |
| Termite | [`themes/termite/Dark Pastel`](themes/termite/Dark%20Pastel) |
| Termux | [`themes/termux/Dark Pastel.properties`](themes/termux/Dark%20Pastel.properties) |
| Tilda | [`themes/tilda/Dark Pastel.itermcolors_config_0`](themes/tilda/Dark%20Pastel.itermcolors_config_0) |
| VHS | [`themes/vhs/Dark Pastel.json`](themes/vhs/Dark%20Pastel.json) |
| Vim | [`themes/vim/Dark Pastel.vim`](themes/vim/Dark%20Pastel.vim) |
| VS Code | [`themes/vscode/Dark Pastel.json`](themes/vscode/Dark%20Pastel.json) |
| Warp | [`themes/warp/Dark Pastel.yaml`](themes/warp/Dark%20Pastel.yaml) |
| Wayst | [`themes/wayst/Dark Pastel`](themes/wayst/Dark%20Pastel) |
| WezTerm | [`themes/wezterm/Dark Pastel.toml`](themes/wezterm/Dark%20Pastel.toml) |
| Windows Terminal | [`themes/windowsterminal/Dark Pastel.json`](themes/windowsterminal/Dark%20Pastel.json) |
| Xfce Terminal | [`themes/xfce4terminal/Dark Pastel.theme`](themes/xfce4terminal/Dark%20Pastel.theme) |
| Xresources | [`themes/Xresources/Dark Pastel`](themes/Xresources/Dark%20Pastel) |
| XRDB | [`themes/xrdb/Dark Pastel.xrdb`](themes/xrdb/Dark%20Pastel.xrdb) |
| Zed | [`themes/zed/Dark Pastel.json`](themes/zed/Dark%20Pastel.json) |

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
