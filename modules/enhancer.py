import language_tool_python
import re

_tool = language_tool_python.LanguageTool('en-US', motherTongue='en', disabled_rules=['WHITESPACE_RULE','UPPERCASE_SENTENCE_START_RULE'])

def enhance(text: str):
    if not text or not text.strip():
        return "⚠️ No text provided."
    t = re.sub(r'\s+', ' ', text).strip()
    try:
        matches = _tool.check(t)
        corrected = language_tool_python.utils.correct(t, matches)
        corrected = corrected.strip()
        if corrected and corrected[-1] not in ".!?":
            corrected += "."
        return corrected
    except Exception as e:
        return f"⚠️ Enhancement failed: {e}"

