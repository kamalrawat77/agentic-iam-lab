from google.colab import userdata

MODEL_NAME = "gemini-2.5-flash"


def get_gemini_key():
    return userdata.get("GEMINI_API_KEY")


def get_github_token():
    return userdata.get("GITHUB_TOKEN")
