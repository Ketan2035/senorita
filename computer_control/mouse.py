import pyautogui


def click():
    """
    Left click.
    """
    pyautogui.click()
    return "Left click performed"


def double_click():
    """
    Double left click.
    """
    pyautogui.doubleClick()
    return "Double click performed"


def right_click():
    """
    Right click.
    """
    pyautogui.rightClick()
    return "Right click performed"


def scroll_up(amount=500):
    """
    Scroll up.
    """
    pyautogui.scroll(amount)
    return f"Scrolled up {amount}"


def scroll_down(amount=500):
    """
    Scroll down.
    """
    pyautogui.scroll(-amount)
    return f"Scrolled down {amount}"
