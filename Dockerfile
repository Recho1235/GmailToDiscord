FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3-pip

# Copy source code to the container
COPY GmailToDiscord.py /app/
COPY requirements.txt /app/
WORKDIR /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Set environment variables
ENV IMAP_SERVER=imap.gmail.com
ENV IMAP_PORT=993
ENV IMAP_USERNAME=test@gmail.com
ENV IMAP_PASSWORD=apppassword
ENV KEYWORDS=key,words,here
ENV DISCORD_WEBHOOK_URL=discord/webhook/url/here

# Run the script
CMD ["python3", "GmailToDiscord.py"]