const inputText = document.getElementById('inputText');
const output = document.getElementById('output');
const player = document.getElementById('player');

document.getElementById('summBtn').onclick = async () => {
  const text = inputText.value.trim();
  if (!text) { output.innerText = "Enter text to summarize."; return; }
  output.innerText = "Summarizing...";
  const res = await fetch('/summarize', { method:'POST', body: new URLSearchParams({ text })});
  const data = await res.json();
  output.innerText = data.result;
};

document.getElementById('enhBtn').onclick = async () => {
  const text = inputText.value.trim();
  if (!text) { output.innerText = "Enter text to enhance."; return; }
  output.innerText = "Enhancing...";
  const res = await fetch('/enhance', { method:'POST', body: new URLSearchParams({ text })});
  const data = await res.json();
  output.innerText = data.result;
};

document.getElementById('emojiBtn').onclick = async () => {
  const text = inputText.value.trim();
  if (!text) { output.innerText = "Enter text to add emojis."; return; }
  output.innerText = "Adding emojis...";
  const res = await fetch('/emoji', { method:'POST', body: new URLSearchParams({ text })});
  const data = await res.json();
  output.innerHTML = data.result;
};

document.getElementById('ttsBtn').onclick = async () => {
  const text = inputText.value.trim();
  if (!text) { output.innerText = "Enter text to read aloud."; return; }
  output.innerText = "Generating audio...";
  const res = await fetch('/tts', { method:'POST', body: new URLSearchParams({ text })});
  const data = await res.json();
  if (data.audio_url) {
    player.style.display = 'block';
    player.src = data.audio_url;
    player.play();
    output.innerText = "Playing audio.";
  } else {
    output.innerText = "TTS failed.";
  }
};

// Recording + upload for STT
let mediaRecorder;
let chunks = [];
const recBtn = document.getElementById('recBtn');
const micStatus = document.getElementById('micStatus');

recBtn.onclick = async () => {
  if (mediaRecorder && mediaRecorder.state === 'recording') {
    mediaRecorder.stop();
    recBtn.innerText = '🎤 Record';
    micStatus.innerText = 'Uploading audio...';
    return;
  }
  // start recording
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    micStatus.innerText = 'Browser does not support audio recording.';
    return;
  }
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    chunks = [];
    mediaRecorder.ondataavailable = e => chunks.push(e.data);
    mediaRecorder.onstop = async () => {
      const blob = new Blob(chunks, { type: 'audio/webm' });
      const form = new FormData();
      const filename = `rec_${Date.now()}.webm`;
      form.append('file', blob, filename);
      micStatus.innerText = 'Uploading...';
      try {
        const res = await fetch('/stt', { method:'POST', body: form });
        const data = await res.json();
        if (data.result) {
          inputText.value = data.result;
          output.innerText = 'Transcription complete — text populated above.';
        } else if (data.error) {
          output.innerText = 'STT error: ' + data.error;
        } else {
          output.innerText = 'STT failed.';
        }
      } catch (err) {
        output.innerText = 'Upload/transcription error: ' + err;
      } finally {
        micStatus.innerText = 'Click 🎤 to record (will upload to server)';
      }
    };
    mediaRecorder.start();
    recBtn.innerText = '⏹ Stop';
    micStatus.innerText = 'Recording... Click mic again to stop.';
  } catch (err) {
    micStatus.innerText = 'Microphone access denied or error.';
  }
};
