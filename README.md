Gmail to Discord
This is a simple script that monitors a Gmail inbox for messages containing specific keywords, and then sends those messages to a Discord webhook.

Usage
Make sure you have Docker installed on your system.

Clone this repository to your local machine:
git clone https://github.com/recho1235/GmailToDiscord.git

Change into the GmailToDiscord directory:
cd GmailToDiscord
    
Replace imap.gmail.com with your IMAP server, 993 with your IMAP port, test@gmail.com with your Gmail account, apppassword with your Gmail app password, key,words,here with the keywords you want to monitor, and discord/webhook/url/here with your Discord webhook URL.

Start the Docker container:

docker-compose up -d
To check the logs, run:

docker-compose logs -f
Press Ctrl + C to exit the logs.

To stop the container, run:

docker-compose down

License
This project is licensed under the MIT License. See the LICENSE file for details.
