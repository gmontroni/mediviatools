<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Can u give me a code with this markdowns?

Absolutely! Below you'll find a ready-to-copy-and-paste **README.md** in Markdown format, including image tags that you can manually place after uploading the screenshots to your GitHub repository.
You’ll need to adjust the `yourusername` and image paths as needed.

# Medivia Tools GUI

## What is Medivia Tools GUI?

**Medivia Tools GUI** is a fast and user-friendly desktop application for Medivia online players, providing essential utilities for organized group hunts, loot sharing, drop/skin probability calculations, and a quick item vendor lookup—all via a beautiful graphical interface!

## Features

### 1. 📦 Supplies Calculator

Easily calculate each player's total supply costs for group hunts.

### 2. 💰 Hunt Profit Divider

Split total loot equally and fairly—calculate how much each player should receive after accounting for waste.

### 3. 🛒 Where to Buy/Sell Items

Search for any item to instantly see which NPC buys/sells it and for how much.

### 4. 🎲 Drop/Skin Probability Calculator

Find the odds of getting rare drops or skins based on drop rate, kills, and quantity desired.

## Installation

### On Ubuntu / Linux

```bash
# 1. Make sure Python 3 and pip are installed
sudo apt update
sudo apt install python3 python3-pip

# 2. (Optional but recommended) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install ttkbootstrap

# 4. Download the project
git clone https://github.com/yourusername/medivia-tools-gui.git
cd medivia-tools-gui

# 5. Run the app
python3 mediviatools-gui.py
```


#### To create a standalone app (optional):

```bash
pip install pyinstaller
pyinstaller --hidden-import "PIL._tkinter_finder" --onefile --windowed mediviatools-gui.py
```


### On Windows

1. [Install Python 3.x](https://www.python.org/downloads/) (check "Add Python to PATH" during installation).
2. Open Windows Command Prompt or PowerShell.
3. Install required packages:

```
pip install ttkbootstrap
```

4. Download and extract the repo .zip or use Git:

```
git clone https://github.com/yourusername/medivia-tools-gui.git
cd medivia-tools-gui
```

5. Run the app:

```
python mediviatools-gui.py
```

6. *(Optional)* To build an `.exe`:

```
pip install pyinstaller
pyinstaller --hidden-import "PIL._tkinter_finder" --onefile --windowed mediviatools-gui.py
```

The `.exe` will appear in the `dist\` folder.

## Project Structure

- **mediviatools-gui.py** — Main Python source file (Tkinter + ttkbootstrap).
- **images/** — Screenshots for showcase.
- No internet or database required; all info local/offline.


## Credits

Created by [matematiico](https://mediviathings.net/characters/search/?name=matematiico)

> Questions, suggestions, or bug reports? Open an issue or send a pull request!

**Tip:**
After uploading your screenshots to your repository (e.g. in an `images` folder), replace the image paths above as needed.

If you want the code block with this README string ready to paste into a `.md` file or a Python variable, let me know!

<div style="text-align: center">⁂</div>

[^1]: Screenshot-from-2025-08-01-15-20-09.jpg

[^2]: Screenshot-from-2025-08-01-15-20-41.jpg

[^3]: Screenshot-from-2025-08-01-15-21-11.jpg

[^4]: Screenshot-from-2025-08-01-15-21-48.jpg

[^5]: mediviatools-gui.py
