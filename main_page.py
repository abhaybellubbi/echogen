from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
import logging

logger = logging.getLogger(__name__)

class EchoGenUI(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        logger.info("EchoGenUI initialized.")
        self.setStyleSheet("background-color: #f0f0f0;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        header = QLabel("🎙️ <b>EchoGen</b>")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 28px;")

        logo_box = QLabel("Here we can ADD logo if required")
        logo_box.setAlignment(Qt.AlignCenter)
        logo_box.setStyleSheet("border: 1px solid gray; padding: 8px; border-radius: 6px;")

        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        welcome = QLabel("Welcome to Voice Studio!")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("font-size: 20px; color: #555;")

        description = QLabel("Convert text to voice or record & listen instantly.")
        description.setAlignment(Qt.AlignCenter)
        description.setStyleSheet("font-size: 16px; color: #666;")

        text_btn = QPushButton("🔉 Text to Speech")
        speech_btn = QPushButton("🎤 Speech to Speech")
        speech_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        for btn in (text_btn, speech_btn):
            btn.setFixedSize(250, 60)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 16px;
                    border: 2px solid gray;
                    border-radius: 10px;
                    background-color: white;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)

        text_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))  # Navigate to TTS

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(text_btn)
        btn_layout.addWidget(speech_btn)

        version_label = QLabel("v1.0.0")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("color: #555; margin-top: 20px;")

        layout.addWidget(header)
        layout.addWidget(logo_box)
        layout.addWidget(line)
        layout.addWidget(welcome)
        layout.addWidget(description)
        layout.addLayout(btn_layout)
        layout.addWidget(version_label)

        self.setLayout(layout)