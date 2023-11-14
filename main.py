import os
import json

import gmail_def
import telegram_def

# Setting DIR for taking credentials, tokens and sender email
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gmail_credentials = os.path.join(BASE_DIR, 'Python-TelegramBot-ErrorNotifier', 'credentials.json')
gmail_token = os.path.join(BASE_DIR, 'Python-TelegramBot-ErrorNotifier', 'token.json')
telegram_token = os.path.join(BASE_DIR, 'Python-TelegramBot-ErrorNotifier', 'telegram_token.json')

with open(telegram_token, 'r') as telegram_token_json:
        telegram_token_dic = json.load(telegram_token_json)

BOT_TOKEN, CHAT_ID, SENDER_EMAIL = telegram_token_dic['bot_token'], telegram_token_dic['group_chat_id'], telegram_token_dic["sender_email"]

# Defining the scope and API version
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
API_VERSION = 'v1'

# Getting new messages from defined sender's mail
new_message_list = gmail_def.main_check_message(gmail_token, SCOPES, API_VERSION, SENDER_EMAIL)

# If any new message, send it to telegram chat
if new_message_list!=None:
    telegram_def.send_telegram_message(new_message_list, BOT_TOKEN, CHAT_ID)
