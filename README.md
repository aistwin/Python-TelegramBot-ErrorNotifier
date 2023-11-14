# telegram-bot

Initial problem - we wanted to be notified about server crashes from Yandex Server through Telegram. However, they did not have out-of-box solution for that

Solution - send alarms to gmail, then take it through API credentials and send to Telegram by token

How it is done:
- Configured alarms in Yandex Cloud, where we sent alarsm to certain email
- Through credentials API, looked for unread messages
- Send alarms emails as messages by POST Request

## Getting started

### Get Telegram Bot token

### Get Gmail API Credentials

### Install requirements

If you have issues with activating venv, try this https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

pip install -r requirements.txt

### Run main.py in venv
