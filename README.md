GmailToDiscord is a Python script that runs in the background and checks a Gmail account for new emails containing specific keywords. If a matching email is found, the script sends a message to a Discord channel using a webhook URL.

The script is designed to run as a Docker container, which simplifies the installation and setup process. The container can be easily configured using environment variables.

To use GmailToDiscord, follow these steps:

Clone the repository to your local machine.

Create a Discord webhook URL for the channel you want to receive messages in. You can find instructions on how to create a webhook URL here.

Create a new file called .env in the root of the project directory.

Set the following environment variables in the .env file:

IMAP_SERVER: The hostname of the IMAP server (e.g. imap.gmail.com).
IMAP_PORT: The port number of the IMAP server (e.g. 993 for Gmail).
IMAP_USERNAME: The email address of the Gmail account to check.
IMAP_PASSWORD: The app password to use for authentication (see these instructions for how to generate an app password).
KEYWORDS: A comma-separated list of keywords to search for in the email subject and body.
DISCORD_WEBHOOK_URL: The webhook URL to use for sending messages to Discord.

Build the Docker image using the following command:

docker build -t recho1235/gmailtodiscord:latest .
Run the Docker container using the following command:

docker run --env-file .env recho1235/gmailtodiscord:latest
This will start the script running in the container.

Environment Variables
Here are the environment variables that can be set in the .env file:

IMAP_SERVER: The hostname of the IMAP server (e.g. imap.gmail.com).
IMAP_PORT: The port number of the IMAP server (e.g. 993 for Gmail).
IMAP_USERNAME: The email address of the Gmail account to check.
IMAP_PASSWORD: The app password to use for authentication (see these instructions for how to generate an app password).
KEYWORDS: A comma-separated list of keywords to search for in the email subject and body.
DISCORD_WEBHOOK_URL: The webhook URL to use for sending messages to Discord.
Note that all of these environment variables are required for the script to work properly.

License
This project is licensed under the MIT License. See the LICENSE file for details.
