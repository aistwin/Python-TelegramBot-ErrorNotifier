def authenticate_gmail(gmail_token, SCOPES, API_VERSION):
    
    import os
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    # Check for the token file
    if os.path.exists(gmail_token):
        creds = Credentials.from_authorized_user_file(gmail_token, SCOPES)
    else:
        # Create the OAuth 2.0 flow for authentication
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for future use
    with open(gmail_token, 'w') as token:
        token.write(creds.to_json())

    return build('gmail', API_VERSION, credentials=creds)


def mark_message_as_read(service, message_id):
    message = service.users().messages().modify(userId='me', id=message_id, body={'removeLabelIds': ['UNREAD']}).execute()
    return message


def main_check_message(gmail_token, SCOPES, API_VERSION, SENDER_EMAIL):

    import datetime

    service = authenticate_gmail(gmail_token, SCOPES, API_VERSION)
    results = service.users().messages().list(userId='me', q=f'from:{SENDER_EMAIL} is:unread').execute()
    messages = results.get('messages', [])

    if not messages:
        return None
    else:
        new_messages = []

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()

            # Extract and display the timestamp
            timestamp_unix = int(msg["internalDate"]) / 1000  # Convert from milliseconds to seconds
            timestamp = datetime.datetime.fromtimestamp(timestamp_unix).strftime('%Y-%m-%d %H:%M:%S')

            # Mark the message as read
            mark_message_as_read(service, message['id'])

            # Creating dic for further appending to list
            new_message = {
                "message_body" : msg["snippet"],
                "message_sent_time" : timestamp
            }

            new_messages.append(new_message)
        
        return new_messages
