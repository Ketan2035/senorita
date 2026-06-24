import threading
import subprocess
import datetime

from voice import speak, listen
from ai import ask_ai
from weather import get_weather
from notes import save_note, show_notes

from system import *
from computer_control import *

from language import (
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

backend_thread.start()


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

        result = press_enter()

        speak(result)


    # =================================
    # PRESS TAB
    # =================================

    elif intent == "press_tab":

        result = press_tab()

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

        result = copy_text()

        speak(result)


    # =================================
    # PASTE
    # =================================

    elif intent == "paste":

        result = paste_text()

        speak(result)


    # =================================
    # SELECT ALL
    # =================================

    elif intent == "select_all":

        result = select_all()

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

    else:

        answer = ask_ai(

            intent_data.get(
                "message",
                english_query
            )

        )

        speak(
            translate_from_english(
                answer,
                user_language
            )
        )

