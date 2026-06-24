import pyttsx3
import speech_recognition as sr
from utilities.language import (
    detect_language,
    translate_to_english,
    translate_from_english
)

engine = pyttsx3.init()

def speak(text):
    print(f"Senorita: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""