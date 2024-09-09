import sys
import datetime
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QHBoxLayout
from PySide6.QtCore import Qt

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setGeometry(100, 100, 400, 500)

        self.light_theme = True

        # Create main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create header layout for buttons
        self.header_layout = QHBoxLayout()
        self.layout.addLayout(self.header_layout)

        # Create Theme Button
        self.theme_button = QPushButton("Switch to Dark Theme")
        self.theme_button.clicked.connect(self.toggle_theme)
        self.header_layout.addWidget(self.theme_button)

        # Create Exit Button
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        self.header_layout.addWidget(self.exit_button)
        self.header_layout.setAlignment(Qt.AlignRight)

        # Create Text Edit for Chat History
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.layout.addWidget(self.chat_history)

        # Create Line Edit for User Input
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Type your message here...")
        self.user_input.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.user_input)

        # Create Send Button
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        # Apply Initial Style
        self.apply_light_theme()

    def toggle_theme(self):
        if self.light_theme:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()
        self.light_theme = not self.light_theme

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #000000;
            }
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-top: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c;
            }
        """)

        self.theme_button.setText("Switch to Dark Theme")
        self.exit_button.setText("Exit")

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #333333;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #ffffff;
            }
            QTextEdit {
                background-color: #555555;
                border: 1px solid #777777;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit {
                border: 1px solid #777777;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-top: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c;
            }
        """)

        self.theme_button.setText("Switch to Light Theme")
        self.exit_button.setText("Exit")

    def send_message(self):
        user_message = self.user_input.text().strip()
        if user_message:
            self.chat_history.append(f"<b>You:</b> {user_message}")
            if user_message.lower() == "bye":
                self.chat_history.append("<b>Chatbot:</b> Goodbye! Have a fantastic day!")
                self.close()
            elif user_message.lower() == "help":
                self.chat_history.append("<b>Chatbot:</b> Here are some commands you can use:\n"
                                         "- 'hello': Greet the chatbot.\n"
                                         "- 'how are you': Ask how the chatbot is.\n"
                                         "- 'what's your name': Learn the chatbot's name.\n"
                                         "- 'what can you do': Get information about the chatbot's capabilities.\n"
                                         "- 'what's the time': Get the current time.\n"
                                         "- 'what's the date': Get the current date.\n"
                                         "- 'tell me a joke': Hear a joke.\n"
                                         "- 'bye': Exit the chat.")
            else:
                response = self.get_response(user_message)
                self.chat_history.append(f"<b>Chatbot:</b> {response}")
            self.user_input.clear()

    def get_response(self, user_input):
        user_input = user_input.lower()

        if user_input == "hello":
            return "Hi there! How can I assist you today?"
        elif user_input == "how are you":
            return "I'm an AI, so I don't have feelings, but I'm here to help you!"
        elif user_input == "what's your name":
            return "I'm Chatbot, your virtual assistant. Nice to meet you!"
        elif user_input == "what can you do":
            return ("I can have a simple conversation with you. You can ask me about the weather, "
                    "the time, or just say 'bye' to end our chat.")
        elif user_input == "what's the time":
            now = datetime.datetime.now()
            return f"The current time is {now.strftime('%H:%M:%S')}."
        elif user_input == "what's the date":
            today = datetime.date.today()
            return f"Today's date is {today.strftime('%Y-%m-%d')}."
        elif user_input == "tell me a joke":
            return "Why don't scientists trust atoms? Because they make up everything!"
        elif user_input.startswith("what is the weather like"):
            return "I can't check the weather right now, but I hope it's sunny where you are!"
        elif user_input.startswith("what is your favorite"):
            if "color" in user_input:
                return "My favorite color is blue!"
            elif "food" in user_input:
                return "I don't eat, but I imagine pizza would be great!"
            else:
                return "I don't have preferences, but I can help with many topics!"
        elif user_input == "who created you":
            return "I was created by a Python enthusiast to demonstrate simple chatbot functionality."
        elif user_input == "what is your purpose":
            return "My purpose is to assist you with information and have a simple conversation."
        elif user_input == "can you help with programming":
            return "Yes, I can help with programming-related questions and provide guidance."
        elif user_input == "bye":
            return "Goodbye! Have a fantastic day!"
        else:
            return "I'm sorry, I don't understand that."

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotGUI()
    window.show()
    sys.exit(app.exec())
