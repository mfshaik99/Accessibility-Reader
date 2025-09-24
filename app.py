from flask import Flask, render_template, request, jsonify
from modules import summarizer, enhancer, emoji_adder, tts, stt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['text']
    summary = summarizer.summarize(text)
    return jsonify({'result': summary})

@app.route('/enhance', methods=['POST'])
def enhance_text():
    text = request.form['text']
    enhanced = enhancer.enhance(text)
    return jsonify({'result': enhanced})

@app.route('/emoji', methods=['POST'])
def add_emoji():
    text = request.form['text']
    emoji_text = emoji_adder.add_emoji(text)
    return jsonify({'result': emoji_text})

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    tts_path = tts.speak(text)
    return jsonify({'audio': tts_path})

@app.route('/stt', methods=['GET'])
def speech_to_text():
    recognized_text = stt.listen()
    return jsonify({'result': recognized_text})

if __name__ == '__main__':
    app.run(debug=True)
