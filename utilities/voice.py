
import speech_recognition as sr
from utilities.language import (
    detect_language,
    translate_to_english,
    translate_from_english
)

 
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("Senorita:",text)
    speaker.Speak(text)

    
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