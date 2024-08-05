import streamlit as st
from io import BytesIO
from streamlit_mic_recorder import mic_recorder
import tempfile

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
        #voice_recording = mic_recorder(start_prompt="Record Audio", stop_prompt="Stop recording", just_once=True)

        #if voice_recording:
            #audio_bytes = voice_recording["bytes"]
            #st.success("Audio recorded successfully!")
            # response= send_audio(audio_bytes)
            # st.markdown(f'**Bot:** {response}')

        # File upload sections
        st.header("📂 Upload PDFs")
        pdf_files = st.file_uploader(
            "Choose PDF files",
            type=["pdf"],
            accept_multiple_files=True
        )

        if pdf_files:
            for pdf_file in pdf_files:
                st.success(f"PDF file '{pdf_file.name}' uploaded successfully.")

        st.header("📸 Upload Images")
        image_files = st.file_uploader(
            "Choose image files",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True
        )

        if image_files:
            for image_file in image_files:
                file_details = {"FileName": image_file.name, "FileType": image_file.type}
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(image_file.getvalue())
                    temp_file_path = temp_file.name
                st.image(image_file, caption=image_file.name, use_column_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Chat container
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Text input and response
        st.header("💬 Chat")
        user_input = st.text_input("You: ", placeholder="Type your message here...", key="text_input")

        if user_input:
            # Placeholder for handling the bot's response
            response = f"This is a placeholder response to: {user_input}"
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