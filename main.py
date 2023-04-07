from utils import get_chat_id, send_message
import json
import requests

def main():
    API_TOKEN: str = input("Enter your Telegram API token: ")

    chat_id: int = get_chat_id(api_token=API_TOKEN)
    send_message(api_token=API_TOKEN, chat_id=chat_id)

if __name__ == "__main__":
    main()