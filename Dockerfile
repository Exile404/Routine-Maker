# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Install system dependencies (including Chrome browser and related tools)
RUN apt-get update && apt-get install -yq wget gnupg2
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -yq google-chrome-stable

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download and install chromedriver
RUN CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip -d /usr/local/bin && \
    rm chromedriver_linux64.zip && \
    chmod +x /usr/local/bin/chromedriver

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for FastAPI to run in production mode
ENV FASTAPI_ENV=production

# Run the FastAPI app when the container launches with quiet log level
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "error"]
