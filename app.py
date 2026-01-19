import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Local Environment (for your ThinkPad)
load_dotenv()

# Configure AI
# Public uses st.secrets, Local uses .env
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-3-flash')

# Page Styling
st.set_page_config(page_title="CyberNavigator AI", page_icon="🛡️", layout="centered")
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; padding: 10px; margin-bottom: 10px; }
    .stChatInputContainer { border-top: 1px solid #ddd; padding-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ CyberNavigator AI")
st.caption("Your personalized guide from total beginner to Cyber Pro.")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Cyber Career Scout. Are you a total beginner, a student, or looking to switch careers into Cybersecurity?"}
    ]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask about cyber careers, tools, or roadmaps..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # Deep research prompt logic
        full_prompt = f"Act as a professional Cybersecurity Career Mentor. The user says: {prompt}. If they are a beginner, explain concepts simply. Provide deep research insights on 2026 market trends, salary ranges, and essential skills."
        
        try:
            response = model.generate_content(full_prompt)
            assistant_response = response.text
            response_placeholder.markdown(assistant_response)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        except Exception as e:
            st.error(f"Error: {e}")