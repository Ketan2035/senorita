import webbrowser


# ==========================================
# Open Website
# ==========================================
def open_website(url):
    """
    Open any website in default browser.
    """
    if not url.startswith("http"):
        url = "https://" + url

    webbrowser.open(url)
    return f"Opening {url}"


# ==========================================
# Google Search
# ==========================================
def search_google(query):
    """
    Search on Google.
    """
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching Google for {query}"


# ==========================================
# YouTube Search
# ==========================================
def search_youtube(query):
    """
    Search on YouTube.
    """
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching YouTube for {query}"


# ==========================================
# GitHub Search
# ==========================================
def search_github(query):
    """
    Search on GitHub.
    """
    url = "https://github.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching GitHub for {query}"


# ==========================================
# LinkedIn Search
# ==========================================
def search_linkedin(query):
    """
    Search on LinkedIn.
    """
    url = "https://www.linkedin.com/search/results/all/?keywords=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching LinkedIn for {query}"


# ==========================================
# Context-Based Search
# ==========================================
def search_in_context(current_site, query):
    """
    Search inside the currently active platform.
    Example: YouTube → YouTube search, GitHub → GitHub search
    """

    current_site = current_site.lower().strip()
    query = query.strip()

    if current_site == "youtube":
        return search_youtube(query)

    elif current_site == "github":
        return search_github(query)

    elif current_site == "linkedin":
        return search_linkedin(query)

    else:
        return search_google(query)


# ==========================================
# Quick Website Shortcuts
# ==========================================
def open_youtube():
    webbrowser.open("https://youtube.com")
    return "Opening YouTube"


def open_google():
    webbrowser.open("https://google.com")
    return "Opening Google"


def open_gmail():
    webbrowser.open("https://mail.google.com")
    return "Opening Gmail"


def open_github():
    webbrowser.open("https://github.com")
    return "Opening GitHub"


def open_chatgpt():
    webbrowser.open("https://chatgpt.com")
    return "Opening ChatGPT"