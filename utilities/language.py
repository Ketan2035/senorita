from langdetect import detect

HINGLISH_WORDS = [
    "mausam",
    "kya",
    "kaise",
    "kitna",
    "kahan",
    "kab",
    "namaste",
    "khol",
    "kholo",
    "batao",
    "mera",
    "meri",
    "mujhe",
    "abhi",
    "youtube",
    "google",
    "note",
    "save",
    "dikhao",
    "chalu",
    "band",
    "karo"
]


def detect_language(text):

    text_lower = text.lower()

    for word in HINGLISH_WORDS:
        if word in text_lower:
            return "hi"

    try:
        return detect(text)
    except:
        return "en"


def translate_to_english(text):
    """
    Currently disabled.
    We let the AI understand Hindi/Hinglish directly.
    """
    return text


def translate_from_english(text, target_language):
    """
    Currently disabled.
    Returns original text.
    """
    return text