import pyautogui
import pygetwindow as gw


def minimize_window():
    """
    Minimize the active window.
    """
    pyautogui.hotkey("win", "down")
    return "Window minimized"


def maximize_window():
    """
    Maximize the active window.
    """
    pyautogui.hotkey("win", "up")
    return "Window maximized"


def restore_window():
    """
    Restore active window.
    """
    pyautogui.hotkey("win", "down")
    return "Window restored"


def close_window():
    """
    Close active window.
    """
    pyautogui.hotkey("alt", "f4")
    return "Window closed"


def switch_window():
    """
    Switch to next window.
    """
    pyautogui.hotkey("alt", "tab")
    return "Switched window"


def next_window():
    """
    Move to next open window.
    """
    pyautogui.hotkey("alt", "esc")
    return "Moved to next window"


def show_desktop():
    """
    Show desktop.
    """
    pyautogui.hotkey("win", "d")
    return "Desktop displayed"


def snap_left():
    """
    Snap current window to left side.
    """
    pyautogui.hotkey("win", "left")
    return "Window snapped left"


def snap_right():
    """
    Snap current window to right side.
    """
    pyautogui.hotkey("win", "right")
    return "Window snapped right"


def move_window_to_next_monitor():
    """
    Move active window to another monitor.
    """
    pyautogui.hotkey("win", "shift", "right")
    return "Window moved to next monitor"


def open_task_view():
    """
    Open Windows Task View.
    """
    pyautogui.hotkey("win", "tab")
    return "Task View opened"


def create_virtual_desktop():
    """
    Create a new virtual desktop.
    """
    pyautogui.hotkey("win", "ctrl", "d")
    return "Virtual desktop created"


def close_virtual_desktop():
    """
    Close current virtual desktop.
    """
    pyautogui.hotkey("win", "ctrl", "f4")
    return "Virtual desktop closed"


def next_virtual_desktop():
    """
    Switch to next virtual desktop.
    """
    pyautogui.hotkey("win", "ctrl", "right")
    return "Switched to next virtual desktop"


def previous_virtual_desktop():
    """
    Switch to previous virtual desktop.
    """
    pyautogui.hotkey("win", "ctrl", "left")
    return "Switched to previous virtual desktop"


def get_active_window():
    """
    Get active window title.
    """
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
        return "No active window found"
    except Exception as e:
        return str(e)


def list_windows():
    """
    List all open window titles.
    """
    try:
        windows = [w.title for w in gw.getAllWindows() if w.title]
        return windows
    except Exception as e:
        return str(e)


def focus_window(title):
    """
    Focus a window by partial title match.
    """
    try:
        for window in gw.getAllWindows():
            if title.lower() in window.title.lower():
                window.activate()
                return f"Focused: {window.title}"

        return f"No window found containing '{title}'"

    except Exception as e:
        return str(e)