import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from modules import summarizer, enhancer, emoji_adder, tts, stt

UPLOAD_FOLDER = "uploads"
AUDIO_FOLDER = "static/audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    text = request.form.get("text", "")
    result = summarizer.summarize(text)
    return jsonify({"result": result})

@app.route("/enhance", methods=["POST"])
def enhance_text():
    text = request.form.get("text", "")
    result = enhancer.enhance(text)
    return jsonify({"result": result})

@app.route("/emoji", methods=["POST"])
def add_emoji():
    text = request.form.get("text", "")
    result = emoji_adder.add_emoji(text)
    return jsonify({"result": result})

@app.route("/tts", methods=["POST"])
def text_to_speech():
    text = request.form.get("text", "")
    filename = tts.speak(text, out_dir=app.config['AUDIO_FOLDER'])
    if not filename:
        return jsonify({"error": "No text provided"}), 400
    return jsonify({"audio_url": f"/{app.config['AUDIO_FOLDER']}/{filename}"})

@app.route("/stt", methods=["POST"])
def speech_to_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    f = request.files['file']
    if f.filename == '':
        return jsonify({"error": "No selected file"}), 400
    filename = secure_filename(f.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(path)
    text = stt.transcribe_file(path)
    return jsonify({"result": text})

@app.route('/static/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # Render port
    app.run(host="0.0.0.0", port=port)
