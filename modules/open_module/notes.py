def save_note(text):

    with open("notes.txt", "a") as f:
        f.write(text + "\n")

    return "Note saved"

def show_notes():

    try:
        with open("notes.txt", "r") as f:
            return f.read()

    except:
        return "No notes found"