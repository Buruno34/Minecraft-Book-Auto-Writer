
# Minecraft Book Auto-Writer

## Overview
This Python script automates the tedious process of writing long texts into "Book and Quill" items in Minecraft. It reads text from a local file, processes it to respect Minecraft's strict formatting limitations, and uses mouse and keyboard macros to paste the text into the game page by page.

## How to Use

1. **Prepare the Files:** Download `main.py` and create a `text.txt` file in the same directory.
2. **Insert Text and Execute:** Paste your desired text into `text.txt`. Run the script, then rapidly switch to your active Minecraft window and ensure your Book and Quill is opened to page 1. *(Note: The script includes a 3-second countdown to give you time to switch windows).*
3. **Wait:** Do not interact with your mouse or keyboard until the automated writing process is completely finished.






## Features
* **Smart Word Wrapping & Pagination:** Automatically divides your text so it fits the in-game limits (maximum 19 characters per line and 14 lines per page) without cutting words in half.
* **Automated Typing:** Utilizes the clipboard and `Ctrl + V` commands to input text instantly, bypassing the need to type out character by character.
* **Auto Page-Turning:** Automatically clicks the right arrow in the book UI to advance to the next page when the current one is full.
* **Built-in Failsafe:** Uses `pyautogui.FAILSAFE`. If the script goes out of control, jam your mouse cursor into any of the four corners of your screen to abort the execution immediately.

## Requirements
* Python 3.x
* Third-party libraries: `pyautogui` and `pyperclip`

Install the required dependencies using pip:
```bash
pip install pyautogui pyperclip