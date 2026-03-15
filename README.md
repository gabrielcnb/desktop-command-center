# desktop-command-center

Minimal Windows 11-style desktop widget with live weather, to-do list, and daily habit tracking.

## Features

- Live weather display via wttr.in (no API key required)
- Persistent to-do list stored locally as JSON
- Daily motivational quote, randomly selected at startup
- Daily habit reminder, randomly selected at startup
- Windows 11 color palette — clean, card-based layout
- Configurable city and country via `data/config.json`
- Windows autostart support via startup folder shortcut
- Draggable window, ESC to close

## Stack

| Component | Choice |
|-----------|--------|
| Language | Python 3 |
| GUI | tkinter (stdlib) |
| Weather API | wttr.in (HTTP, no auth) |
| HTTP client | requests |
| Persistence | JSON files |

## Setup / Installation

```bash
pip install requests
```

No additional dependencies beyond the Python standard library and requests.

## Usage

```bash
python command_center.py
```

On first run, `data/config.json` is created with defaults:

```json
{
  "city": "São Paulo",
  "country_code": "BR"
}
```

Edit this file before launching to change the weather location.

To-do items are saved automatically to `data/todos.json` and persist between sessions.

**Autostart on Windows:**

1. Press `Win + R`, type `shell:startup`, press Enter
2. Copy the `Command Center.lnk` shortcut into that folder

Alternatively, double-click `run.bat` to launch without a terminal window.

## File Structure

```
command-center/
├── command_center.py   # Main application
├── run.bat             # Launch script (no terminal window)
└── data/
    ├── config.json     # City configuration (auto-created on first run)
    └── todos.json      # To-do list (auto-created on first run)
```
