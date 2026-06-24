import subprocess
import os
import shutil


APPS = {
    # Windows Built-in Apps
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "ms paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "terminal": "wt.exe",
    "explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "registry editor": "regedit.exe",
    "device manager": "devmgmt.msc",
    "services": "services.msc",
    "disk management": "diskmgmt.msc",

    # Browsers
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",

    # Development Tools
    "vscode": "code",
    "visual studio code": "code",

    # Communication
    "discord": "discord.exe",
    "telegram": "telegram.exe",
    "whatsapp": "whatsapp.exe",

    # Media
    "spotify": "spotify.exe",
    "vlc": "vlc.exe",

    # Gaming
    "steam": "steam.exe",
}


def open_app(app_name):
    """
    Open an application by name.
    """

    app_name = app_name.lower().strip()

    if app_name in APPS:
        target = APPS[app_name]

        try:
            subprocess.Popen(target, shell=True)
            return f"Opening {app_name}"

        except Exception as e:
            return f"Error opening {app_name}: {e}"

    # Try finding executable automatically
    path = shutil.which(app_name)

    if path:
        try:
            subprocess.Popen(path)
            return f"Opening {app_name}"

        except Exception as e:
            return f"Error opening {app_name}: {e}"

    return f"Could not find '{app_name}'"


def open_path(path):
    """
    Open any executable or file path.
    """

    try:
        os.startfile(path)
        return f"Opened {path}"

    except Exception as e:
        return str(e)


def open_folder(folder_path):
    """
    Open a folder.
    """

    try:
        os.startfile(folder_path)
        return f"Opened folder {folder_path}"

    except Exception as e:
        return str(e)


def run_command(command):
    """
    Run a terminal command.
    """

    try:
        subprocess.Popen(command, shell=True)
        return f"Running: {command}"

    except Exception as e:
        return str(e)


if __name__ == "__main__":

    print(open_app("notepad"))
    print(open_app("calculator"))
    print(open_app("chrome"))
    print(open_app("vscode"))