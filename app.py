import streamlit as st
from io import BytesIO
from streamlit_mic_recorder import mic_recorder
import requests

FLASK_URL = "https://749b-34-168-139-200.ngrok-free.app/text"

def get_bot_response(prompt):
    response = requests.post(FLASK_URL, json={'prompt': prompt})
    
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('output', 'No response from server')
    else:
        return f"Error: {response.status_code}"


def main():
    st.set_page_config(page_title="SSC Chatbot", layout="wide")

    # Custom CSS for ChatGPT-like UI
    st.markdown("""
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
        }
        .chat-box {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .user-input {
            margin-bottom: 20px;
        }
        .left-panel {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            max-width: 200px;
            margin-right: 20px;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: black;
            text-align: center;
            padding: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("🤖 SSC Chatbot Application")

    # Create two columns: one for the left panel and one for the chat
    col1, col2 = st.columns([1, 2])

    with col1:
        # Left panel for voice recording and file upload
        st.markdown('<div class="left-panel">', unsafe_allow_html=True)

        # Voice recording
        st.header("🎤 Voice Recording")
        voice_recording = mic_recorder(start_prompt="Record Audio", stop_prompt="Stop recording", just_once=True)

        if voice_recording:
            audio_bytes = voice_recording["bytes"]
            st.success("Audio recorded successfully!")
            # response= send_audio(audio_bytes)
            # st.markdown(f'**Bot:** {response}')

        # File upload sections
        st.header("📂 Upload PDFs")
        pdf_file = st.file_uploader(
            "Choose PDF files",
            type=["pdf"],
            accept_multiple_files=False
        )

        if pdf_file:
            st.success(f"PDF file has been uploaded successfully.")

        st.header("📸 Upload Images")
        image_file = st.file_uploader(
            "Choose image files",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=False
        )

        if image_file:
            st.image(image_file, use_column_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Chat container
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Text input and response
        st.header("💬 Chat")
        user_input = st.text_input("You: ", placeholder="Type your message here...", key="text_input")

        if user_input:
            # Placeholder for handling the bot's response
            response = get_bot_response(user_input)
            st.markdown(f'<div class="chat-box">Bot: "{response}"</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>Developed with ❤️ by B Rahul Naik</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()