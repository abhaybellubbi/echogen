🎙️ Start The Voice – EchoGen

    An intuitive voice studio in Python (PyQt5) for Text-to-Speech and Speech-to-Text.

✨ Overview

Start The Voice – EchoGen is a lightweight desktop application that lets you:

✅ Convert Text to Speech
✅ Record Speech and Transcribe to Text
✅ Navigate with a clean, modern interface

Built using Python 3 and PyQt5, this project is perfect for learning voice processing or building custom voice tools.
📸 Screenshots

**Welcome Page**  
![Welcome Page](screenshots/welcome_page.png)

**Main Menu**  
![Main Menu](screenshots/main_menu.png)

**Text to Speech**  
![Text to Speech](screenshots/text_to_speech.png)

**Speech to Text**  
![Speech to Text](screenshots/speech_to_text.png)
⚙️ Requirements

Python 3.7+

Install dependencies:

pip install -r requirements.txt

requirements.txt:

PyQt5
SpeechRecognition
PyAudio

    On Linux, also run:

    sudo apt install portaudio19-dev python3-pyaudio

🚀 Running the Application

Clone this repository:

git clone https://github.com/your-username/start-the-voice.git
cd start-the-voice

Run:

python echogen_main.py

🖥️ Usage

1️⃣ Welcome Page

    Click 🚀 START THE VOICE to enter the app.

2️⃣ Main Menu

    🔉 Text to Speech: Convert text input to spoken audio.

    🎤 Speech to Text: Record and transcribe speech.

3️⃣ Text to Speech Page

    Type text.

    Play or save the audio.

    Return to the main menu.

4️⃣ Speech to Text Page

    Start recording.

    View transcription.

    Return to the main menu.

📂 Project Structure

/start-the-voice/
├── echogen_main.py             # Entry point
├── main_page.py                # Main menu
├── text_to_speech_page.py      # Text-to-Speech
├── speech_to_text_page.py      # Speech-to-Text
├── echogen.log                 # Logs
├── requirements.txt            # Dependencies
├── README.md                   # Project info
└── assets/                     # (Optional images or audio)

📝 Logging

All activity is logged in echogen.log:

    Page navigation

    Button actions

    Transcription status

🛠️ Extending

Ideas for enhancement:

    Support Whisper / DeepSpeech for more accurate transcription.

    Multiple voice languages.

    Dark mode themes.

    Export transcriptions as files.

✨ About the Project

Start The Voice – EchoGen was created to make voice processing approachable and customizable for everyone.
👥 Authors

    Abhay

    Bhuvan

    Santoshi

📄 License

This project is licensed under the MIT License – see the LICENSE file for details.
⭐️ Support

If you like this project, please ⭐️ the repo and share your feedback!
