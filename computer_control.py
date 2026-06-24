import pyautogui
import datetime
import os
import psutil
import subprocess
import time


pyautogui.FAILSAFE = True


def click():
    pyautogui.click()
    return "Clicked"


def double_click():
    pyautogui.doubleClick()
    return "Double clicked"


def right_click():
    pyautogui.rightClick()
    return "Right clicked"


def scroll_up():
    pyautogui.scroll(500)
    return "Scrolled up"


def scroll_down():
    pyautogui.scroll(-500)
    return "Scrolled down"


def press_enter():
    pyautogui.press("enter")
    return "Pressed enter"


def press_tab():
    pyautogui.press("tab")
    return "Pressed tab"


def type_text(text):
    pyautogui.write(text, interval=0.05)
    return f"Typed {text}"




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



# def close_app(app_name):
#     try:
#         app_name = app_name.lower()

#         for proc in psutil.process_iter(['pid', 'name']):
#             name = proc.info['name']

#             if name and app_name in name.lower():
#                 proc.kill()
#                 return f"Closed {name}"

#         return f"No running app found for {app_name}"

#     except Exception as e:
#         return str(e)


def close_window():
    pyautogui.hotkey('alt', 'f4')
    return "Closed active window"


def minimize_window():
    pyautogui.hotkey('win', 'down')
    return "Minimized active window"


def maximize_window():
    pyautogui.hotkey('win', 'up')
    return "Maximized active window"


def switch_window():
    pyautogui.hotkey('alt', 'tab')
    return "Switched window"


def switch_tab():
    pyautogui.hotkey('ctrl', 'tab')
    return "Switched tab"


def previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    return "Switched to previous tab"


def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    return "Closed tab"

def new_tab():
    pyautogui.hotkey('ctrl', 't')
    return "Opened new tab"


def reopen_closed_tab():
    pyautogui.hotkey('ctrl', 'shift', 't')
    return "Reopened closed tab"


def select_all():
    pyautogui.hotkey('ctrl', 'a')
    return "Selected all"


def copy():
    pyautogui.hotkey('ctrl', 'c')
    return "Copied"


def paste():
    pyautogui.hotkey('ctrl', 'v')
    return "Pasted"


def cut():
    pyautogui.hotkey('ctrl', 'x')
    return "Cut"


def save():
    pyautogui.hotkey('ctrl', 's')
    return "Saved"


def undo():
    pyautogui.hotkey('ctrl', 'z')
    return "Undo"


def redo():
    pyautogui.hotkey('ctrl', 'y')
    return "Redo"


import pyautogui
import time

def play_first_video():

    time.sleep(5)  # YouTube results load hone do

    pyautogui.press("tab", presses=24)
    time.sleep(1)

    pyautogui.press("enter")

    return "Playing first video"