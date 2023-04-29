Gmail to Discord Webhook

This Python script connects to a Gmail account via IMAP, searches for emails containing specified keywords, and sends these emails as embeds to a Discord webhook URL.
Getting Started

To use this script, you will need to have the following modules installed:

    imaplib
    email
    requests
    html2text

You can install these modules using pip:

pip install imaplib email requests html2text

You will also need to provide the following information in the script:

# IMAP settings
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
IMAP_USERNAME = 'your-gmail-username'
IMAP_PASSWORD = 'your-gmail-app-password'

# Discord webhook settings
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/your-webhook-url'

Make sure to replace your-gmail-username with your Gmail username and your-gmail-app-password with an App Password if you have 2-step verification enabled on your Gmail account. Also, replace your-webhook-url with your Discord webhook URL.
Usage

    Run the script using a Python interpreter:

python gmail-to-discord.py

    The script will connect to your Gmail account via IMAP, search for emails containing the specified keywords, and send these emails as embeds to the Discord webhook URL.

License

This project is licensed under the MIT License - see the LICENSE file for details.
