import sys
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt
from main_page import EchoGenUI
from text_to_speech_page import TextToSpeechPage
from speech_to_text_page import SpeechToTextPage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='echogen.log',
    filemode='w'
)
logger = logging.getLogger(__name__)

class WelcomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(40)

        welcome_label = QLabel("🎙️ WELCOME TO START THE VOICE")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 26px; color: #333;")

        start_button = QPushButton("🚀 START THE VOICE")
        start_button.setFixedSize(220, 60)
        start_button.setStyleSheet("""
            font-size: 18px;
            border-radius: 10px;
            background-color: #1976D2;
            color: white;
        """)
        start_button.clicked.connect(self.goto_main_ui)

        layout.addStretch()
        layout.addWidget(welcome_label)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)
        layout.addStretch()

        self.setLayout(layout)

    def goto_main_ui(self):
        logger.info("Navigating to EchoGen UI")
        self.stacked_widget.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()

    welcome_page = WelcomePage(stacked_widget)
    main_page = EchoGenUI(stacked_widget)
    text_speech = TextToSpeechPage(stacked_widget)
    speech_speech = SpeechToTextPage(stacked_widget)

    stacked_widget.addWidget(welcome_page)   # Index 0
    stacked_widget.addWidget(main_page)      # Index 1
    stacked_widget.addWidget(text_speech)    # Index 2
    stacked_widget.addWidget(speech_speech)    # Index 3

    stacked_widget.setFixedSize(800, 600)
    stacked_widget.show()

    logger.info("App launched.")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()