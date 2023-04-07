import requests
import json
from typeguard import typechecked

@typechecked
def get_chat_id(api_token: str):
    # create the URL for the getUpdates method
    url: str = f"https://api.telegram.org/bot{api_token}/getUpdates"

    # send a GET request to the URL
    response: requests.Response = requests.get(url)

    # parse the response as JSON
    data: dict = json.loads(response.content)

    # get the chat ID of the most recent message
    chat_id: int = data["result"][-1]["message"]["chat"]["id"]

    return chat_id

@typechecked
def send_message(api_token: str, chat_id: int):
    # set the URL for the sendMessage method
    url: str = f"https://api.telegram.org/bot{api_token}/sendMessage"

    # set the message text and payload
    message: str = "requestid:1"
    payload: dict = {"chat_id": chat_id, "text": message}

    # send a POST request to the URL with the payload
    response: requests.Response = requests.post(url, data=payload)

    # print the response content
    print(response.content)