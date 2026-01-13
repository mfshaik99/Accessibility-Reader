import streamlit as st
from ai_functions import summarize_text, enhance_text, add_emojis

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Accessibility Reader",
    page_icon="🔊",
    layout="wide"
)

# ---------- Browser Text-to-Speech ----------
def speak_text(text: str):
    if text.strip():
        # Browser TTS using Web Speech API
        st.markdown(f"""
        <script>
        var msg = new SpeechSynthesisUtterance(`{text}`);
        window.speechSynthesis.speak(msg);
        </script>
        """, unsafe_allow_html=True)

# ---------- CSS Styling ----------
st.markdown("""
<style>
/* Gradient Background */
body {
    background: linear-gradient(135deg, #FFDEE9, #B5FFFC);
    font-family: 'Segoe UI', sans-serif;
}

/* Center Title */
.title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 20px;
    color: #333;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    margin-bottom: 25px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.18);
}

/* Animated Buttons */
.stButton>button {
    background: linear-gradient(45deg, #FF8C94, #6A82FB);
    color: white;
    font-weight: 600;
    border-radius: 12px;
    padding: 12px 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
}

/* Footer */
.footer {
    text-align: center;
    color: #333;
    font-weight: 700;
    margin-top: 50px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">AI Accessibility Reader</div>', unsafe_allow_html=True)

# ---------- Input Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
input_text = st.text_area(
    "Enter your text here:",
    height=220,
    placeholder="Paste long text here..."
)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Action Buttons Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
result = ""

with col1:
    if st.button("📝 Summarize", use_container_width=True):
        if input_text.strip():
            result = summarize_text(input_text)
        else:
            st.warning("Please enter some text!")

with col2:
    if st.button("✨ Enhance", use_container_width=True):
        if input_text.strip():
            result = enhance_text(input_text)
        else:
            st.warning("Please enter some text!")

with col3:
    if st.button("😊 Add Emojis", use_container_width=True):
        if input_text.strip():
            result = add_emojis(input_text)
        else:
            st.warning("Please enter some text!")

with col4:
    if st.button("🔊 Read Input", use_container_width=True):
        if input_text.strip():
            speak_text(input_text)
        else:
            st.warning("Please enter some text!")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Output Card ----------
if result:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Result")
    st.text_area("Output:", value=result, height=240)

    if "quota exceeded" in result.lower():
        st.warning("Gemini free-tier limit reached. Try again later.")

    if st.button("🔊 Read Result"):
        speak_text(result)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">Created by Team Smart Minds</div>', unsafe_allow_html=True)
