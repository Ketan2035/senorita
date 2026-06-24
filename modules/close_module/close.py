# ==========================
# APPLICATION CONTROLS
# ==========================

def close_app(app_name):

    app_name = app_name.lower()

    for proc in psutil.process_iter(['pid', 'name']):

        try:

            name = proc.info['name']

            if name and app_name in name.lower():

                proc.kill()

                return f"Closed {name}"

        except:
            pass

    return f"{app_name} is not running"


def close_chrome():
    return close_app("chrome")


def close_vscode():
    return close_app("code")


def close_notepad():
    return close_app("notepad")


def close_cmd():
    return close_app("cmd")


