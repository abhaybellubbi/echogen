from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
import logging

logger = logging.getLogger(__name__)

class TextToSpeechPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        logger.info("TextToSpeechPage initialized.")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🔉 Text to Speech")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        voice_label = QLabel("Select the Voice")
        voice_input = QLineEdit("INDIAN")
        voice_input.setAlignment(Qt.AlignCenter)
        voice_input.setFixedWidth(150)

        text_label = QLabel("Enter the Text")
        text_box = QTextEdit()
        text_box.setPlaceholderText("Enter the Text")

        btn_layout = QHBoxLayout()

        play_btn = QPushButton("▶️ Play")
        save_btn = QPushButton("💾 Save Audio")
        back_btn = QPushButton("⬅️ Back")

        for btn in (play_btn, save_btn, back_btn):
            btn.setFixedSize(130, 40)

        back_btn.clicked.connect(self.go_back)

        btn_layout.addWidget(play_btn)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(back_btn)

        status = QLabel("Status : Audio generation completed / Audio in progress / Audio incomplete")
        status.setStyleSheet("color: gray; font-size: 12px;")
        status.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(voice_label)
        layout.addWidget(voice_input, alignment=Qt.AlignCenter)
        layout.addWidget(text_label)
        layout.addWidget(text_box)
        layout.addLayout(btn_layout)
        layout.addWidget(status)

        self.setLayout(layout)

    def go_back(self):
        logger.info("Back to EchoGenUI from TTS page.")
        self.stacked_widget.setCurrentIndex(1)