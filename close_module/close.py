import os
import tkinter as tk
import subprocess
import psutil
import pyautogui


def close_app(app_name):
    """
    Close running application by name.
    """

    app_name = app_name.lower().strip()

    closed = False

    for proc in psutil.process_iter(['name']):

        try:
            name = proc.info['name']

            if name and app_name in name.lower():
                proc.kill()
                closed = True

        except:
            pass

    if closed:
        return f"Closed {app_name}"

    return f"No running app found for {app_name}"

 
def close_all_windows():
    """
    Attempts to close current active windows repeatedly.
    """
    for _ in range(3):
        pyautogui.hotkey("alt", "f4")

    return "Closed multiple windows"

 

def close_browser():
    """
    Close entire browser window
    """
    pyautogui.hotkey("alt", "f4")
    return "Browser closed"

 


 


def shutdown_pc():
    root = tk.Tk()
    root.title("Shutdown Warning")

    # Window size
    window_width = 600
    window_height = 280

    # Get screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate center position
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set window size and position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Keep popup on top
    root.attributes("-topmost", True)
    root.resizable(False, False)

    # Bring window to front
    root.lift()
    root.focus_force()

    shutdown_cancelled = {"value": False}
    countdown = {"seconds": 10}

    def cancel_shutdown():
        shutdown_cancelled["value"] = True
        root.destroy()

    def shutdown_now():
        root.destroy()
        subprocess.call("shutdown /s /t 0", shell=True)

    title_label = tk.Label(
        root,
        text="⚠ Shutdown Warning ⚠",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=15)

    message_label = tk.Label(
        root,
        text="Your PC will shut down in 10 seconds.\nClick Cancel to stop it.",
        font=("Arial", 12)
    )
    message_label.pack(pady=10)

    countdown_label = tk.Label(
        root,
        text=f"Time Remaining: {countdown['seconds']}s",
        font=("Arial", 14, "bold")
    )
    countdown_label.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    tk.Button(
        btn_frame,
        text="Cancel",
        command=cancel_shutdown,
        width=15,
        height=5
    ).pack(side="left", padx=15)

    tk.Button(
        btn_frame,
        text="Shutdown Now",
        command=shutdown_now,
        width=15,
        height=5
    ).pack(side="left", padx=15)

    def update_countdown():
        if shutdown_cancelled["value"]:
            return

        countdown_label.config(
            text=f"Time Remaining: {countdown['seconds']}s"
        )

        if countdown["seconds"] <= 0:
            root.destroy()
            subprocess.call("shutdown /s /t 0", shell=True)
            return

        countdown["seconds"] -= 1
        root.after(1000, update_countdown)

    update_countdown()

    root.mainloop()

    if shutdown_cancelled["value"]:
        return "Shutdown cancelled."

    return "System shutting down."





 


def restart_pc():
    root = tk.Tk()
    root.title("Restart Warning")

    # Window size
    window_width = 600
    window_height = 280

    # Center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Keep popup on top
    root.attributes("-topmost", True)
    root.resizable(False, False)

    root.lift()
    root.focus_force()

    restart_cancelled = {"value": False}
    countdown = {"seconds": 10}

    def cancel_restart():
        restart_cancelled["value"] = True
        root.destroy()

    def restart_now():
        root.destroy()
        subprocess.call("shutdown /r /t 0", shell=True)

    title_label = tk.Label(
        root,
        text="⚠ Restart Warning ⚠",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=15)

    message_label = tk.Label(
        root,
        text="Your PC will restart in 10 seconds.\nClick Cancel to stop it.",
        font=("Arial", 12)
    )
    message_label.pack(pady=10)

    countdown_label = tk.Label(
        root,
        text=f"Time Remaining: {countdown['seconds']}s",
        font=("Arial", 14, "bold")
    )
    countdown_label.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    tk.Button(
        btn_frame,
        text="Cancel",
        command=cancel_restart,
        width=15,
        height=2
    ).pack(side="left", padx=15)

    tk.Button(
        btn_frame,
        text="Restart Now",
        command=restart_now,
        width=15,
        height=2
    ).pack(side="left", padx=15)

    def update_countdown():
        if restart_cancelled["value"]:
            return

        countdown_label.config(
            text=f"Time Remaining: {countdown['seconds']}s"
        )

        if countdown["seconds"] <= 0:
            root.destroy()
            subprocess.call("shutdown /r /t 0", shell=True)
            return

        countdown["seconds"] -= 1
        root.after(1000, update_countdown)

    update_countdown()

    root.mainloop()

    if restart_cancelled["value"]:
        return "Restart cancelled."

    return "System restarting."


def sleep_pc():
    root = tk.Tk()
    root.title("Sleep Warning")

    # Window size
    window_width = 600
    window_height = 280

    # Center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Keep popup on top
    root.attributes("-topmost", True)
    root.resizable(False, False)

    root.lift()
    root.focus_force()

    sleep_cancelled = {"value": False}
    countdown = {"seconds": 10}

    def cancel_sleep():
        sleep_cancelled["value"] = True
        root.destroy()

    def sleep_now():
        root.destroy()
        subprocess.call(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
            shell=True
        )

    title_label = tk.Label(
        root,
        text="⚠ Sleep Warning ⚠",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=15)

    message_label = tk.Label(
        root,
        text="Your PC will go to sleep in 10 seconds.\nClick Cancel to stop it.",
        font=("Arial", 12)
    )
    message_label.pack(pady=10)

    countdown_label = tk.Label(
        root,
        text=f"Time Remaining: {countdown['seconds']}s",
        font=("Arial", 14, "bold")
    )
    countdown_label.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    tk.Button(
        btn_frame,
        text="Cancel",
        command=cancel_sleep,
        width=15,
        height=2
    ).pack(side="left", padx=15)

    tk.Button(
        btn_frame,
        text="Sleep Now",
        command=sleep_now,
        width=15,
        height=2
    ).pack(side="left", padx=15)

    def update_countdown():
        if sleep_cancelled["value"]:
            return

        countdown_label.config(
            text=f"Time Remaining: {countdown['seconds']}s"
        )

        if countdown["seconds"] <= 0:
            root.destroy()
            subprocess.call(
                "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
                shell=True
            )
            return

        countdown["seconds"] -= 1
        root.after(1000, update_countdown)

    update_countdown()

    root.mainloop()

    if sleep_cancelled["value"]:
        return "Sleep cancelled."

    return "System going to sleep."

def lock_pc():
    """
    Lock system screen
    """
    subprocess.call("rundll32.exe user32.dll,LockWorkStation", shell=True)
    return "System locked"