import os
import subprocess

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "vscode": r"C:\Users\ketan\AppData\Local\Programs\Microsoft VS Code\Code.exe",

    "notepad": "notepad.exe",

    "calculator": "calc.exe",

    "paint": "mspaint.exe",

    "cmd": "cmd.exe",

    "explorer": "explorer.exe"
}


def open_app(app_name):

    app_name = app_name.lower()

    if app_name in APPS:

        try:

            subprocess.Popen(APPS[app_name])

            return f"Opening {app_name}"

        except Exception as e:

            return str(e)
    

    return f"I could not find {app_name}"