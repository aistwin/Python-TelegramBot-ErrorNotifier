def send_telegram_message(messages, BOT_TOKEN, CHAT_ID):
    import requests

    for message in messages:

        message_body = message['message_body']
        message_time = message['message_sent_time']

        # Create a dictionary with the message data
        bot_message = str("Error : " + message_body + "\n" + "Time : " + message_time)
        #telegram_api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        telegram_api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={bot_message}"
        response = requests.post(telegram_api_url)
