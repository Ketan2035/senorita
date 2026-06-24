
import webbrowser
import subprocess
import os
import pyautogui
import psutil




# ==========================================
# Context Memory
# ==========================================

CURRENT_APP = None
CURRENT_WEBSITE = None


# ==========================================
# Apps & Websites Database
# ==========================================

APPS = {

    # Websites
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
    "chatgpt": "https://chatgpt.com",
    "leetcode": "https://leetcode.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "stackoverflow": "https://stackoverflow.com",
    "instagram": "https://instagram.com",
    "facebook": "https://facebook.com",
    "twitter": "https://x.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon": "https://amazon.in",
    "flipkart": "https://flipkart.com",

    # Windows Apps
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "mspaint": "mspaint.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "terminal": "wt.exe",

    # Developer Tools
    "vscode": r"C:\Users\ketan\AppData\Local\Programs\Microsoft VS Code\Code.exe",
}


# ==========================================
# Open App
# ==========================================

def open_app(app_name):

    global CURRENT_APP
    global CURRENT_WEBSITE

    app_name = app_name.lower().strip()

    if app_name not in APPS:
        return f"I could not find {app_name}"

    target = APPS[app_name]

    try:

        if target.startswith("http"):

            webbrowser.open(target)

            CURRENT_WEBSITE = app_name
            CURRENT_APP = app_name

        else:

            subprocess.Popen(target)

            CURRENT_APP = app_name

        return f"Opening {app_name}"

    except Exception as e:

        return f"Error opening {app_name}: {str(e)}"
    



def close_app(app_name):

    app_name = app_name.lower().strip()

    PROCESS_MAP = {

        "chrome": ["chrome.exe"],
        "youtube": ["chrome.exe"],
        "google": ["chrome.exe"],
        "gmail": ["chrome.exe"],
        "github": ["chrome.exe"],
        "linkedin": ["chrome.exe"],
        "chatgpt": ["chrome.exe"],

        "vscode": ["code.exe"],
        "notepad": ["notepad.exe"],
        "calculator": ["calculatorapp.exe", "calc.exe"],
        "cmd": ["cmd.exe"],
        "powershell": ["powershell.exe"],
        "explorer": ["explorer.exe"],
        "mspaint": ["mspaint.exe"],
        "terminal": ["windowsterminal.exe", "wt.exe"]
    }

    targets = PROCESS_MAP.get(app_name)

    if not targets:
        targets = [app_name + ".exe"]

    closed = []

    for proc in psutil.process_iter(['pid', 'name']):

        try:

            proc_name = proc.info['name']

            if not proc_name:
                continue

            if proc_name.lower() in [
                p.lower() for p in targets
            ]:

                proc.kill()

                closed.append(proc_name)

        except:
            pass

    if closed:

        return (
            f"Closed {', '.join(closed)}"
        )

    return (
        f"No running process found for {app_name}"
    )


# ==========================================
# Search Current Context
# ==========================================
def search_youtube(query):

    url = (
        "https://www.youtube.com/results?search_query="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)

    return f"Searching YouTube for {query}"


def search_current_app(query):

    global CURRENT_APP

    query = query.strip()

    if CURRENT_APP == "youtube":

        url = (
            "https://www.youtube.com/results?search_query="
            + query.replace(" ", "+")
        )

        webbrowser.open(url)

        return f"Searching YouTube for {query}"

    elif CURRENT_APP == "github":

        url = (
            "https://github.com/search?q="
            + query.replace(" ", "+")
        )

        webbrowser.open(url)

        return f"Searching GitHub for {query}"

    elif CURRENT_APP == "linkedin":

        url = (
            "https://www.linkedin.com/search/results/all/?keywords="
            + query.replace(" ", "+")
        )

        webbrowser.open(url)

        return f"Searching LinkedIn for {query}"

    else:

        return search_google(query)


# ==========================================
# Google Search
# ==========================================

def search_google(query):

    url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)

    return f"Searching Google for {query}"


# ==========================================
# Open Website
# ==========================================

def open_website(url):

    if not url.startswith("http"):
        url = "https://" + url

    webbrowser.open(url)

    return f"Opening {url}"


# ==========================================
# Browser Controls
# ==========================================

def new_tab():

    pyautogui.hotkey("ctrl", "t")

    return "New tab opened"


def close_tab():

    pyautogui.hotkey("ctrl", "w")

    return "Tab closed"


def reopen_tab():

    pyautogui.hotkey("ctrl", "shift", "t")

    return "Last tab reopened"


def refresh_page():

    pyautogui.press("f5")

    return "Page refreshed"


# ==========================================
# Window Controls
# ==========================================

def close_window():

    pyautogui.hotkey("alt", "f4")

    return "Window closed"


def switch_window():

    pyautogui.hotkey("alt", "tab")

    return "Switched window"


# ==========================================
# Close Application
# ==========================================

def close_app(app_name):

    app_name = app_name.lower()

    for proc in psutil.process_iter(['name']):

        try:

            name = proc.info['name']

            if name and app_name in name.lower():

                proc.kill()

                return f"Closed {name}"

        except:
            pass

    return f"{app_name} is not running"


# ==========================================
# Power Controls
# ==========================================

def shutdown_pc():

    subprocess.call("shutdown /s /t 5")

    return "Shutting down computer"


def restart_pc():

    subprocess.call("shutdown /r /t 5")

    return "Restarting computer"


def lock_pc():

    subprocess.call(
        "rundll32.exe user32.dll,LockWorkStation"
    )

    return "Locking computer"


# ==========================================
# Open Folder
# ==========================================

def open_folder(path):

    try:

        os.startfile(path)

        return f"Opening folder {path}"

    except Exception as e:

        return str(e)


# ==========================================
# Run Command
# ==========================================

def run_command(command):

    try:

        subprocess.Popen(command)

        return f"Running {command}"

    except Exception as e:

        return str(e)
