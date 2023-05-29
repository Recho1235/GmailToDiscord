FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy the script and config file to the container
COPY GmailToDiscord.py /app/
COPY config.yaml /app/

# Install dependencies
RUN pip install pyyaml requests

# Set environment variable
ENV CONFIG_FILE=/app/config.yaml

# Run the script
CMD ["python3", "GmailToDiscord.py"]

