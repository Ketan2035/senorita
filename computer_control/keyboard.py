import pyautogui
import os
import datetime

def type_text(text):
    """
    Type text using keyboard.
    """
    pyautogui.write(text)
    return f"Typed: {text}"


def press_key(key):
    """
    Press a single key.
    """
    pyautogui.press(key)
    return f"Pressed {key}"


def hotkey(*keys):
    """
    Press multiple keys together.
    Example: hotkey("ctrl", "c")
    """
    pyautogui.hotkey(*keys)
    return f"Pressed {' + '.join(keys)}"


def key_down(key):
    """
    Hold a key down.
    """
    pyautogui.keyDown(key)
    return f"Held {key}"


def key_up(key):
    """
    Release a held key.
    """
    pyautogui.keyUp(key)
    return f"Released {key}"


def enter():
    pyautogui.press("enter")
    return "Pressed Enter"


def backspace():
    pyautogui.press("backspace")
    return "Pressed Backspace"


def delete():
    pyautogui.press("delete")
    return "Pressed Delete"


def tab():
    pyautogui.press("tab")
    return "Pressed Tab"


def escape():
    pyautogui.press("esc")
    return "Pressed Escape"


def space():
    pyautogui.press("space")
    return "Pressed Space"


def copy():
    pyautogui.hotkey("ctrl", "c")
    return "Copied selected text"


def paste():
    pyautogui.hotkey("ctrl", "v")
    return "Pasted from clipboard"


def cut():
    pyautogui.hotkey("ctrl", "x")
    return "Cut selected text"


def undo():
    pyautogui.hotkey("ctrl", "z")
    return "Undo"


def redo():
    pyautogui.hotkey("ctrl", "y")
    return "Redo"


def select_all():
    pyautogui.hotkey("ctrl", "a")
    return "Selected all"


def save():
    pyautogui.hotkey("ctrl", "s")
    return "Saved"


def find(text=None):
    pyautogui.hotkey("ctrl", "f")

    if text:
        pyautogui.write(text)

    return "Opened Find"


def new_tab():
    pyautogui.hotkey("ctrl", "t")
    return "Opened new tab"


def close_tab():
    pyautogui.hotkey("ctrl", "w")
    return "Closed tab"


def reopen_tab():
    pyautogui.hotkey("ctrl", "shift", "t")
    return "Reopened closed tab"


def switch_tab(direction="next"):
    if direction == "next":
        pyautogui.hotkey("ctrl", "tab")
        return "Switched to next tab"

    pyautogui.hotkey("ctrl", "shift", "tab")
    return "Switched to previous tab"


def refresh():
    pyautogui.press("f5")
    return "Refreshed page"


def screenshot_shortcut():
    pyautogui.hotkey("win", "shift", "s")
    return "Opened screenshot tool"


def task_manager():
    pyautogui.hotkey("ctrl", "shift", "esc")
    return "Opened Task Manager"


def lock_screen():
    pyautogui.hotkey("win", "l")
    return "Locked screen"


def show_desktop():
    pyautogui.hotkey("win", "d")
    return "Showing desktop"


def alt_tab():
    pyautogui.hotkey("alt", "tab")
    return "Switched window"


def close_window():
    pyautogui.hotkey("alt", "f4")
    return "Closed window"


def screenshot():
    folder = r"C:\Users\ketan\OneDrive\Pictures\Screenshots 1"

    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Unique filename
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    # Full path
    filepath = os.path.join(folder, filename)

    # Take and save screenshot
    image = pyautogui.screenshot()
    image.save(filepath)

    return f"Screenshot saved at {filepath}"

