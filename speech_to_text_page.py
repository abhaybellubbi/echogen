from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import speech_recognition as sr
import logging
import threading

logger = logging.getLogger(__name__)

class SpeechToTextPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.recognizer = sr.Recognizer()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🎤 Speech to Text")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Your transcribed text will appear here...")
        self.text_area.setReadOnly(True)

        self.status_label = QLabel("Status: Waiting for input...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 12px; color: gray;")

        btn_layout = QHBoxLayout()

        record_btn = QPushButton("🎙️ Start Recording")
        back_btn = QPushButton("⬅️ Back")
        for btn in (record_btn, back_btn):
            btn.setFixedSize(180, 50)

        record_btn.clicked.connect(self.start_recording)
        back_btn.clicked.connect(self.go_back)

        btn_layout.addWidget(record_btn)
        btn_layout.addWidget(back_btn)

        layout.addWidget(title)
        layout.addWidget(self.text_area)
        layout.addLayout(btn_layout)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def start_recording(self):
        self.status_label.setText("Status: Listening...")
        threading.Thread(target=self.record_and_transcribe).start()

    def record_and_transcribe(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                self.status_label.setText("Status: Processing...")
                text = self.recognizer.recognize_google(audio)
                self.text_area.setText(text)
                self.status_label.setText("Status: Transcription complete.")
                logger.info("Speech recognized: %s", text)
        except sr.UnknownValueError:
            self.status_label.setText("Status: Could not understand audio.")
        except sr.RequestError:
            self.status_label.setText("Status: Recognition service error.")
        except Exception as e:
            self.status_label.setText(f"Status: Error - {str(e)}")
            logger.error("Speech recognition error: %s", e)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(1)
