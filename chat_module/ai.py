import requests
from utilities.config import BACKEND_URL

def ask_ai(message):

    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": message}
        )

        return response.json()["reply"]

    except Exception as e:
        return str(e)