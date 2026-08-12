# app/chatbot.py

from app.config import WELCOME_MESSAGE, EXIT_MESSAGE
from app.conversation import Conversation
from app.ollama_client import OllamaClient


class ChatBot:

    def __init__(self):
        self.conversation = Conversation()
        self.client = OllamaClient()

    def start(self):

        print(WELCOME_MESSAGE)

        while True:

            user_input = input("\nYou : ")

            if user_input.lower() == "exit":
                print(EXIT_MESSAGE)
                break

            # Save user's message
            self.conversation.add_user_message(user_input)

            # Get AI response
            ai_reply = self.client.get_response(
                self.conversation.get_messages()
            )

            # Save AI response
            self.conversation.add_ai_message(ai_reply)

            # Print AI response
            print(f"\nAI : {ai_reply}")