import language_tool_python
import re

_tool = language_tool_python.LanguageTool('en-US')

def enhance(text: str):
    if not text or not text.strip():
        return "⚠️ No text provided."
    # Basic cleanup
    t = re.sub(r'\s+', ' ', text).strip()
    try:
        matches = _tool.check(t)
        corrected = language_tool_python.utils.correct(t, matches)
        # Small style improvements: ensure sentences end properly
        corrected = corrected.strip()
        if corrected and corrected[-1] not in ".!?":
            corrected += "."
        return corrected
    except Exception as e:
        return f"⚠️ Enhancement failed: {e}"
