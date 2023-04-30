import imaplib
import email
import requests
import html2text
import time

# IMAP settings
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
IMAP_USERNAME = 'your-username@gmail.com'
IMAP_PASSWORD = 'your-app-password'
KEYWORDS = 'your,keywords,here'

keywords_list = KEYWORDS.split(',')

# Discord webhook settings
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/your/discord/webhook/url'

# Connect to Gmail account via IMAP
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(IMAP_USERNAME, IMAP_PASSWORD)
mail.select('inbox')

# Search for emails containing specified keywords
while True:
    typ, msgnums = mail.search(None, 'UNSEEN')
    for msgnum in msgnums[0].split()[::-1]:  # reverse order to get oldest first
        typ, msg_data = mail.fetch(msgnum, '(RFC822)')

        # Parse email and extract relevant information
        msg = email.message_from_bytes(msg_data[0][1])
        from_email = email.utils.parseaddr(msg['From'])[1]
        subject = msg['Subject']
        body = None

        # Check for HTML or rich text body
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                # Plain text body
                body = part.get_payload(decode=True).decode('iso-8859-1')
                break
            elif content_type == 'text/html':
                # HTML body
                html = part.get_payload(decode=True).decode()
                h = html2text.HTML2Text()
                h.ignore_links = True
                body = h.handle(html)
                break

        # If body is still None, use an empty string instead
        if body is None:
            body = ""

        # Check if email contains any of the specified keywords
        if not any(keyword in subject.lower() or keyword in body.lower() for keyword in keywords_list):
            # Email does not contain any of the specified keywords, so skip it
            continue

        # Send email to Discord via webhook
        data = {
            'embeds': [
                {
                    'author': {
                        'name': from_email,
                        'icon_url': f'https://www.gravatar.com/avatar/{hash(from_email.lower())}?d=identicon'
                    },
                    'title': subject,
                    'description': body,
                    'color': 3066993
                }
            ]
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code != 204:
            print(f'Error sending message to Discord webhook: {response.text}')

    # Wait 1800 seconds before checking for new mail again
    time.sleep(1800)