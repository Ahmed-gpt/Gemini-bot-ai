import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Custom Styling
st.set_page_config(page_title="Gemini Bot AI", page_icon="🤖", layout="centered")

# Custom CSS for ChatGPT-style interface
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stApp {
        background-color: #0e1117;
    }
    .title-style {
        text-align: center;
        color: #61dafb;
        font-size: 36px;
        margin-bottom: 0;
    }
    .subtitle-style {
        text-align: center;
        color: #cccccc;
        font-size: 18px;
        margin-top: 0;
    }
    .chat-bubble-user {
        background-color: #1f2937;
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: right;
        color: white;
    }
    .chat-bubble-bot {
        background-color: #374151;
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: left;
        color: white;
    }
    .input-box {
        border: 2px solid #61dafb;
        border-radius: 10px;
        padding: 10px;
        width: 100%;
        background-color: #1f2937;
        color: white;
    }
    .stButton>button {
        background-color: #61dafb;
        color: black;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        border-radius: 10px;
    }
    img {
        display: block;
        margin: auto;
        width: 150px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load and display logo
st.image("logo.png")

# Title
st.markdown('<h1 class="title-style">Gemini Bot AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-style">Powered by Google Gemini 1.5 Flash</p>', unsafe_allow_html=True)

# Chat History State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
user_input = st.text_input("🧠 Enter your prompt here:", key="input", label_visibility="collapsed")

# Submit Button
if st.button("Ask Gemini"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_input)
                output = response.text

                # Add to chat history
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Gemini", output))

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Display Chat History
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f'<div class="chat-bubble-user"><strong>You:</strong><br>{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-bot"><strong>Gemini Says:</strong><br>{message}</div>', unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center><sub>Built with ❤️ using Google Gemini API and Streamlit</sub></center>", unsafe_allow_html=True)
