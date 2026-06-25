import threading
import subprocess
import datetime
from open_module.app import open_app, open_folder, run_command
from computer_control import *
from open_module.browser import *
from close_module.close import *
from utilities.voice import *

from utilities.language import (
    detect_language,
    translate_to_english,
    translate_from_english
)

from brain import get_intent

def start_backend():
    subprocess.run(["python", "app.py"])


# Start Flask backend
backend_thread = threading.Thread(
    target=start_backend,
    daemon=True
)

# backend_thread.start()


# Greeting
hour = datetime.datetime.now().hour

if hour < 12:
    speak("Good Morning sir how can i help you")

elif hour < 18:
    speak("Good Afternoon sir how can i help you")

else:
    speak("Good Evening sir how can i help you")

speak("I am Senorita. Ready to help you.")


while True:

    query = listen()

    if not query:
        continue

    try:

        user_language = detect_language(query)

        english_query = translate_to_english(query)

        print("\n====================")
        print("Original :", query)
        print("Language :", user_language)
        print("English  :", english_query)
        print("====================\n")

    except Exception as e:

        print("Language Error:", e)

        user_language = "en"
        english_query = query

    try:

        intent_data = get_intent(english_query)

        print("Intent:", intent_data)

        intent = intent_data.get(
            "intent",
            "chat"
        )

    except Exception as e:

        print("Brain Error:", e)

        intent = "chat"

        intent_data = {
            "message": english_query
        }

    # =================================
    # EXIT
    # =================================

    if intent == "exit":

        speak(
            translate_from_english(
                "Goodbye. Have a nice day.",
                user_language
            )
        )

        break

    # =================================
    # OPEN APP
    # =================================

    elif intent == "open_app":

        app_name = intent_data.get("app")

        if not app_name:

            speak(
                "Which application should I open?"
            )

            continue

        websites = {
            # ======================
            # BASIC DAILY USE
            # ======================
            "youtube": open_youtube,
            "google": open_google,
            "gmail": open_gmail,
            "chatgpt": open_chatgpt,

            # ======================
            # SOCIAL / COMMUNICATION
            # ======================
            "instagram": lambda: open_website("https://instagram.com"),
            "facebook": lambda: open_website("https://facebook.com"),
            "twitter": lambda: open_website("https://x.com"),
            "linkedin": lambda: open_website("https://linkedin.com"),
            "whatsapp": lambda: open_website("https://web.whatsapp.com"),
            "telegram": lambda: open_website("https://web.telegram.org"),
            "github": lambda: open_website("https://github.com/Ketan2035"),

            # ======================
            # STUDY / CODING
            # ======================
            "leetcode": lambda: open_website("https://leetcode.com"),
            "geeksforgeeks": lambda: open_website("https://geeksforgeeks.org"),
            "stackoverflow": lambda: open_website("https://stackoverflow.com"),
            "wikipedia": lambda: open_website("https://wikipedia.org"),

            # ======================
            # AI TOOLS
            # ======================
            "gemini": lambda: open_website("https://gemini.google.com"),
            "claude": lambda: open_website("https://claude.ai"),
            "perplexity": lambda: open_website("https://perplexity.ai"),

            # ======================
            # PRODUCTIVITY
            # ======================
            "notion": lambda: open_website("https://notion.so"),
            "trello": lambda: open_website("https://trello.com"),
            "figma": lambda: open_website("https://figma.com"),
            "canva": lambda: open_website("https://canva.com"),

            # ======================
            # CLOUD / STORAGE
            # ======================
            "google drive": lambda: open_website("https://drive.google.com"),
            "dropbox": lambda: open_website("https://dropbox.com"),
            "onedrive": lambda: open_website("https://onedrive.live.com"),

            # ======================
            # ENTERTAINMENT
            # ======================
            "netflix": lambda: open_website("https://netflix.com"),
            "prime video": lambda: open_website("https://primevideo.com"),
            "spotify": lambda: open_website("https://open.spotify.com"),

            # ======================
            # LEARNING / COURSES
            # ======================
            "udemy": lambda: open_website("https://udemy.com"),
            "coursera": lambda: open_website("https://coursera.org"),
            "edx": lambda: open_website("https://edx.org"),

            # ======================
            # DEV / DEPLOYMENT
            # ======================
            "vercel": lambda: open_website("https://vercel.com"),
            "netlify": lambda: open_website("https://netlify.com"),
            "replit": lambda: open_website("https://replit.com"),

            # ======================
            # UTILITIES
            # ======================
            "google_translate": lambda: open_website("https://translate.google.com"),
            "google maps": lambda: open_website("https://maps.google.com"),
            "weather": lambda: open_website("https://weather.com"),
        }

        if app_name in websites:
            result = websites[app_name]()
        else:
            result = open_app(app_name)

        speak(result)

    # =================================
    # WEATHER
    # =================================

    elif intent == "weather":

        city = intent_data.get("city")

        if not city:

            speak(
                translate_from_english(
                    "Tell me city name",
                    user_language
                )
            )

            city = listen()

            if not city:

                speak(
                    "I did not hear the city name."
                )

                continue

        weather_reply = get_weather(city)

        speak(
            translate_from_english(
                weather_reply,
                user_language
            )
        )

    # =================================
    # SAVE NOTE
    # =================================

    elif intent == "save_note":

        note = intent_data.get("content")

        if not note:

            speak(
                translate_from_english(
                    "What should I save?",
                    user_language
                )
            )

            note = listen()

            if not note:

                speak(
                    "I did not hear any note."
                )

                continue

        result = save_note(note)

        speak(
            translate_from_english(
                result,
                user_language
            )
        )

    # =================================
    # SHOW NOTES
    # =================================

    elif intent == "show_notes":

        notes = show_notes()

        speak(
            translate_from_english(
                notes,
                user_language
            )
        )

    # =================================
    # CLICK
    # =================================

    elif intent == "click":

        result = click()

        speak(result)


    # =================================
    # DOUBLE CLICK
    # =================================

    elif intent == "double_click":

        result = double_click()

        speak(result)


    # =================================
    # RIGHT CLICK
    # =================================

    elif intent == "right_click":

        result = right_click()

        speak(result)


    # =================================
    # SCROLL UP
    # =================================

    elif intent == "scroll_up":

        result = scroll_up()

        speak(result)


    # =================================
    # SCROLL DOWN
    # =================================

    elif intent == "scroll_down":

        result = scroll_down()

        speak(result)


    # =================================
    # PRESS ENTER
    # =================================

    elif intent == "press_enter":

        result = enter()

        speak(result)


    # =================================
    # PRESS TAB
    # =================================

    elif intent == "press_tab":

        result = tab()

        speak(result)


    # =================================
    # TYPE TEXT
    # =================================

    elif intent == "type_text":

        text = intent_data.get("text")

        if not text:

            speak("What should I type?")

            continue

        result = type_text(text)

        speak(result)


    # =================================
    # SCREENSHOT
    # =================================

    elif intent == "screenshot":

        result = screenshot()

        speak(result)


    # =================================
    # MINIMIZE WINDOW
    # =================================

    elif intent == "minimize_window":

        result = minimize_window()

        speak(result)


    # =================================
    # MAXIMIZE WINDOW
    # =================================

    elif intent == "maximize_window":

        result = maximize_window()

        speak(result)


    # =================================
    # CLOSE WINDOW
    # =================================

    elif intent == "close_window":

        result = close_window()

        speak(result)


    # =================================
    # SWITCH WINDOW
    # =================================

    elif intent == "switch_window":

        result = switch_window()

        speak(result)


    # =================================
    # COPY
    # =================================

    elif intent == "copy":

        result = copy()

        speak(result)


    # =================================
    # PASTE
    # =================================

    elif intent == "paste":

        result = paste()

        speak(result)


    # =================================
    # SELECT ALL
    # =================================

    elif intent == "select_all":

        result = select_all()

        speak(result)

    #=================================
    #  close tab
    #=================================

    elif intent == "close_tab":

        result = close_tab()

        speak(result)

    # =================================
    # UNDO
    # =================================
    elif intent == "undo":

        result = undo()

        speak(result)


    # =================================
    # REDO
    # =================================
    elif intent == "redo":

        result = redo()

        speak(result)


    # =================================
    # SAVE
    # =================================
    elif intent == "save":

        result = save()

        speak(result)


    # =================================
    # NEW TAB
    # =================================
    elif intent == "open new_tab":

        result = new_tab()

        speak(result)


    # =================================
    # RESTORE WINDOW
    # =================================
    elif intent == "restore_window":

        result = restore_window()

        speak(result)


    # =================================
    # LOCK SCREEN
    # =================================
    elif intent == "lock_screen":

        result = lock_screen()

        speak(result)


    # =================================
    # REFRESH
    # =================================
    elif intent == "refresh":

        result = refresh()

        speak(result)


    # =================================
    # SWITCH TAB
    # =================================
    elif intent == "switch_tab":

        result = switch_tab()

        speak(result)


    # =================================
    # REOPEN TAB
    # =================================
    elif intent == "reopen_tab":

        result = reopen_tab()

        speak(result)        
    # =================================
    # RUN COMMAND
    # =================================

    elif intent == "run_command":

        command = intent_data.get("command")

        if not command:

            speak("Command not found")

            continue

        result = run_command(command)

        speak(result)


     # =================================
    # CLOSE APP
    # =================================

    elif intent == "close_app":

        app_name = intent_data.get("app")

        if not app_name:
            speak("Which app should I close?")
            continue

        result = close_app(app_name)
        speak(result)


    # =================================
    # CLOSE ALL WINDOWS
    # =================================

    elif intent == "close_all_windows":

        result = close_all_windows()
        speak(result)


    # =================================
    # CLOSE BROWSER
    # =================================

    elif intent == "close_browser":

        result = close_browser()
        speak(result)


    # =================================
    # SHUTDOWN
    # =================================

    elif intent == "shutdown":

        result = shutdown_pc()
        speak(result)


    # =================================
    # RESTART
    # =================================

    elif intent == "restart":

        result = restart_pc()
        speak(result)


    # =================================
    # SLEEP
    # =================================

    elif intent == "sleep":

        result = sleep_pc()
        speak(result)


    # =================================
    # LOCK
    # =================================

    elif intent == "lock":

        result = lock_pc()
        speak(result)        


    # =================================
    # WORKFLOW
    # =================================

    elif intent == "workflow":
        steps = intent_data.get("steps", [])
        for step in steps:
            action = step.get("action")

            print("Executing:", action)

            if action == "open_app":

                result = open_app(step["app"])
                speak(result)

            elif action == "search_youtube":

                result = search_youtube(
                    step["query"]
                )

                speak(result)

            elif action == "play_first_video":

                result = play_first_video()

                speak(result)

            elif action == "click":

                speak(click())

            elif action == "double_click":

                speak(double_click())



    
    # =================================
    # CHAT
    # =================================

    # else:

    #     answer = ask_ai(

    #         intent_data.get(
    #             "message",
    #             english_query
    #         )

    #     )

    #     speak(
    #         translate_from_english(
    #             answer,
    #             user_language
    #         )
    #     )

