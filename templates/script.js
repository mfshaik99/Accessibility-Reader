const feature = document.getElementById("feature");
const textInput = document.getElementById("textInput");
const audioInput = document.getElementById("audioInput");
const processBtn = document.getElementById("processBtn");
const outputText = document.getElementById("outputText");
const audioPlayer = document.getElementById("audioPlayer");

feature.addEventListener("change", () => {
    if (feature.value === "stt") {
        textInput.style.display = "none";
        audioInput.style.display = "block";
    } else if (feature.value === "tts") {
        textInput.style.display = "block";
        audioInput.style.display = "none";
    } else {
        textInput.style.display = "block";
        audioInput.style.display = "none";
    }
});

processBtn.addEventListener("click", async () => {
    const selected = feature.value;
    const text = textInput.value;
    const file = audioInput.files[0];
    
    outputText.innerHTML = "⏳ Processing...";
    audioPlayer.style.display = "none";

    let response = "";
    
    if (selected === "stt") {
        if (!file) { outputText.innerHTML = "⚠️ Please select an audio file."; return; }
        const formData = new FormData();
        formData.append("file", file);
        const res = await fetch("/stt", { method: "POST", body: formData });
        response = await res.text();
    } else {
        const res = await fetch(`/${selected}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });
        response = await res.text();
    }

    if (selected === "tts" && response) {
        audioPlayer.src = `/static/audio/${response}`;
        audioPlayer.style.display = "block";
        outputText.innerHTML = "";
    } else {
        outputText.innerHTML = response;
    }
});
