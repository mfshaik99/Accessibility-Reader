import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# ⚠️ Since you said private repo, key is hardcoded
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Gemini 2.5 Flash (Batch mode)
model = genai.GenerativeModel("gemini-2.5-flash")


def _quota_message():
    return (
        "⚠️ Gemini API quota exceeded.\n\n"
        "This project uses the free tier.\n"
        "Please wait a few minutes and try again."
    )


def summarize_text(text: str) -> str:
    try:
        response = model.generate_content(
            f"Summarize the following text in simple language:\n\n{text}"
        )
        return response.text
    except ResourceExhausted:
        return _quota_message()


def enhance_text(text: str) -> str:
    try:
        response = model.generate_content(
            f"Improve grammar, clarity, and readability:\n\n{text}"
        )
        return response.text
    except ResourceExhausted:
        return _quota_message()


def add_emojis(text: str) -> str:
    try:
        response = model.generate_content(
            f"Add relevant emojis without changing the meaning:\n\n{text}"
        )
        return response.text
    except ResourceExhausted:
        return _quota_message()
