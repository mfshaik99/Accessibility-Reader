# AI Accessibility Reader 🔊

AI Accessibility Reader is a Streamlit-based web application designed to improve content accessibility. It allows users to summarize long text, enhance readability, add meaningful emojis, and listen to text using browser-based text-to-speech.

This project is built as a college academic project with a focus on accessibility, usability, and modern UI design.

---

## ✨ Features

- 📝 Text Summarization – Condenses long text into a short, clear summary  
- ✨ Text Enhancement – Fixes grammatical errors and improves readability  
- 😊 Emoji Enrichment – Adds relevant emojis to improve engagement  
- 🔊 Text-to-Speech – Reads text aloud using browser-based speech synthesis  
- 🎨 Modern UI – Card-based layout with animations and colorful background  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Google Gemini API (gemini-2.5-flash – Batch API)  
- HTML/CSS (for animations and styling)  
- Browser Web Speech API (for Text-to-Speech)  

---

## 📁 Project Structure

ai-accessibility-reader/
│
├── app.py              # Streamlit UI with animations and browser TTS  
├── ai_functions.py     # Gemini AI text processing functions  
├── requirements.txt    # Project dependencies  
├── README.md           # Project documentation  
└── LICENSE             # MIT License  

---

## ▶️ How to Run Locally

1. Clone the repository  
   git clone <your-repo-url>  
   cd ai-accessibility-reader  

2. Install dependencies  
   pip install -r requirements.txt  

3. Add your Google Gemini API key  
   Open ai_functions.py and paste your API key:
   
   GOOGLE_API_KEY = "YOUR_API_KEY_HERE"

4. Run the application  
   streamlit run app.py  

---

## ☁️ Deployment

- Deployed on Render (Free Plan)  
- Uses browser-based text-to-speech (no server-side audio dependencies)  
- Start command:
  
  streamlit run app.py  

---

## 📌 Example Use Case

- Assisting users with reading difficulties  
- Making long articles easier to understand  
- Improving accessibility for visually impaired users  
- Educational content simplification  

---

## 🎓 Academic Note

This project is developed as an educational/college project to demonstrate:
- AI-powered text processing  
- Accessibility-focused UI design  
- Practical cloud deployment using Streamlit  

---

## 👨‍💻 Team

Created by Team Smart Minds

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project with attribution.
