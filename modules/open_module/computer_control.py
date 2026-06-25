import pyautogui
import datetime
import os
import psutil
import subprocess
import time
import modules.open_app.system as system

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



# ==========================
# TAB CONTROLS
# ==========================

def close_tab():
    pyautogui.hotkey("ctrl", "w")
    return "Tab closed"


def close_all_tabs():
    pyautogui.hotkey("ctrl", "shift", "w")
    return "Attempted to close all tabs"


def reopen_closed_tab():
    pyautogui.hotkey("ctrl", "shift", "t")
    return "Reopened closed tab"


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


# ==========================
# SYSTEM POWER
# ==========================

def shutdown_pc():

    subprocess.call(
        "shutdown /s /t 5",
        shell=True
    )

    return "Shutting down PC in 5 seconds"


def restart_pc():

    subprocess.call(
        "shutdown /r /t 5",
        shell=True
    )

    return "Restarting PC in 5 seconds"


def cancel_shutdown():

    subprocess.call(
        "shutdown /a",
        shell=True
    )

    return "Shutdown cancelled"


def lock_pc():

    subprocess.call(
        "rundll32.exe user32.dll,LockWorkStation",
        shell=True
    )

    return "Computer locked"


def sleep_pc():

    subprocess.call(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
        shell=True
    )

    return "Computer sleeping"


def hibernate_pc():

    subprocess.call(
        "shutdown /h",
        shell=True
    )

    return "Computer hibernating"


def sign_out():

    subprocess.call(
        "shutdown /l",
        shell=True
    )

    return "Signing out"


# ==========================
# TASK MANAGER
# ==========================

def open_task_manager():

    subprocess.Popen("taskmgr.exe")

    return "Opening Task Manager"


# ==========================
# SCREEN CONTROL
# ==========================

def screen_off():

    subprocess.call(
        'powershell (Add-Type \'[DllImport("user32.dll")]public static extern int SendMessage(int hWnd,int hMsg,int wParam,int lParam);\' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)',
        shell=True
    )

    return "Screen turned off"
