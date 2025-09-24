# AI-Powered Accessibility Reader

Features:
- Summarization (Transformer-based)
- Grammar & style enhancement (LanguageTool)
- Dynamic emoji addition (no hard-coded emoji mapping)
- Text-to-speech (gTTS fallback pyttsx3)
- Speech-to-text (browser record → upload → server-side transcription)

## Setup
1. Install ffmpeg on your OS (required by pydub).
2. Create venv, install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
