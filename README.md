#  Senorita AI Desktop Assistant

Senorita is a voice-controlled AI desktop assistant built with Python. It can understand voice commands, converse using AI, control your computer, automate browsers, open applications, manage notes, provide weather updates, and execute multi-step workflows.

---

##  Features

###  Voice Assistant

* Speech-to-Text
* Text-to-Speech
* Continuous voice listening
* Supports English, Hindi, and Hinglish commands

###  AI Brain

* Powered by Groq LLM
* Intent detection
* Workflow generation
* Natural language understanding

###  Desktop Control

* Open applications
* Close applications
* Close windows
* Switch windows
* Minimize/Maximize windows
* Open folders
* Run system commands

###  Mouse Control

* Click
* Double Click
* Right Click
* Scroll Up
* Scroll Down

###  Keyboard Control

* Type text
* Press Enter
* Press Tab
* Copy
* Paste
* Cut
* Undo
* Redo
* Save
* Select All

###  Browser Automation

* Open websites
* Google Search
* YouTube Search
* GitHub Search
* LinkedIn Search
* Open new tabs
* Close tabs
* Reopen closed tabs

###  YouTube Automation

Example:

"Senorita open YouTube and search for Arijit Singh songs and play it"

The assistant can:

1. Open YouTube
2. Search for the requested content
3. Play the first video automatically

###  Weather

Get live weather information for any city.

###  Notes

* Save notes
* Read notes

###  Screenshots

Take screenshots using voice commands.

###  Workflows

Example:

"Senorita open YouTube and search for Java tutorial"

The AI converts this into a workflow and executes all steps automatically.

---

#  Project Structure

```text
senorita/

│
├── main.py
├── brain.py
├── voice.py
├── config.py
├── language.py
│
│   ├── computer_control/
│   │   ├── mouse.py
│   │   ├── keyboard.py
│   │   ├── window.py
│   │
│   ├── open_module/
│   │   ├── app_launcher.py
│   │   ├── websites.py
│   │   ├── folders.py
│   │   ├── browser.py
│   │   └── __init__.py
│   │
│   ├── close_module/
│   │   ├── apps.py
│   │   ├── windows.py
│   │   ├── tabs.py
│   │   ├── power.py
│   │   └── __init__.py
│   │
│   └── chat_module/
│       ├── assistant.py
│       ├── memory.py
│       ├── notes.py
│       ├── conversation.py
│       └── __init__.py
│
├── data/
│   ├── notes.txt
│   ├── memory.json
│   └── history.json
│
└── logs/
    └── senorita.log
```

---

#  Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd senorita
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create .env File

Create a file named:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key
```

---

#  API Keys Required

## Groq API

Create account:

https://console.groq.com

Generate API key and add it to `.env`.

---

## Weather API

You can use OpenWeather:

https://openweathermap.org/api

Generate API key and add it to `.env`.

---

#  Run The Project

```bash
python main.py
```

---

#  Example Commands

## Open Apps

```text
Senorita open vscode

Senorita open notepad

Senorita open calculator
```

---

## Browser

```text
Senorita open youtube

Senorita open github

Senorita open linkedin
```

---

## Search

```text
Senorita search Java tutorial

Senorita search Spring Boot roadmap
```

---

## YouTube Automation

```text
Senorita open youtube and search for Kesariya

Senorita play Arijit Singh songs on YouTube
```

---

## Weather

```text
Senorita what's the weather in Delhi

Senorita Bhopal weather
```

---

## Notes

```text
Senorita save note buy milk

Senorita show notes
```

---

## Computer Control

```text
Senorita click

Senorita double click

Senorita scroll down

Senorita press enter

Senorita take screenshot
```

---

## Window Control

```text
Senorita close window

Senorita switch window

Senorita minimize window

Senorita maximize window
```

---

#  Workflow Example

Input:

```text
Senorita open YouTube and search for Java tutorial and play first video
```

Generated Workflow:

```json
{
  "intent": "workflow",
  "steps": [
    {
      "action": "open_app",
      "app": "youtube"
    },
    {
      "action": "search_youtube",
      "query": "Java tutorial"
    },
    {
      "action": "play_first_video"
    }
  ]
}
```

---

#  Technologies Used

* Python
* Groq LLM
* Selenium
* PyAutoGUI
* SpeechRecognition
* Pyttsx3
* Flask
* Requests
* PSUtil
* LangDetect
* Deep Translator

---

#  Disclaimer

This project can control mouse, keyboard, browser, and applications on your computer.

Use carefully and do not execute untrusted commands.

---

#  Future Improvements

* Memory System
* OCR Screen Reading
* File Management
* WhatsApp Automation
* Email Automation
* AI Agent Planning
* Smart Context Awareness
* Multi-Agent Architecture
* RAG Memory System

---

#  Author

Ketan Kumar

Built with Python, AI, and Automation.
