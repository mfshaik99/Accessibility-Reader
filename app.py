from flask import Flask, render_template, request, send_from_directory, jsonify
from modules import summarizer, enhancer, emoji_adder, tts, stt
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

# Summarize
@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "")
    result = summarizer.summarize(text)
    return result

# Enhance
@app.route("/enhance", methods=["POST"])
def enhance_text():
    data = request.get_json()
    text = data.get("text", "")
    result = enhancer.enhance(text)
    return result

# Add Emojis
@app.route("/emoji", methods=["POST"])
def add_emoji_text():
    data = request.get_json()
    text = data.get("text", "")
    result = emoji_adder.add_emoji(text)
    return result

# Text-to-Speech
@app.route("/tts", methods=["POST"])
def text_to_speech():
    data = request.get_json()
    text = data.get("text", "")
    filename = tts.speak(text)
    if filename:
        return filename
    return "⚠️ TTS failed."

# Speech-to-Text
@app.route("/stt", methods=["POST"])
def speech_to_text():
    if "file" not in request.files:
        return "⚠️ No file uploaded."
    file = request.files["file"]
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    text = stt.transcribe_file(path)
    os.remove(path)
    return text

# Serve audio files
@app.route("/static/audio/<path:filename>")
def serve_audio(filename):
    return send_from_directory("static/audio", filename)

if __name__ == "__main__":
    app.run(debug=True)
