# Telegram Bot API Example
This is a Python script that demonstrates how to use the Telegram Bot API to send a message to a specific chat ID.

## Requirements
Python 3.6 or later
1. requests
2. typeguard

## Installation
To install the requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Usage
1. Clone this repository to your local machine.

2. In the project directory, run the following command:


```bash
python main.py
```

3. When prompted, enter your Telegram API token.

4. The script will then use the API token to get the chat ID of the first chat that your bot is a member of.

5. Finally, the script will send a test message to the chat ID using the API token.

That's it! You should see the test message appear in the chat. You can modify the message text and other parameters by editing the send_message() function in the utils.py file.