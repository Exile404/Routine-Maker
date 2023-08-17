# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install ChromeDriver dependencies and Chrome
RUN apt-get update && \
    apt-get install -y wget unzip libglib2.0-0 libnss3 libx11-6 && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || true && \
    apt-get -f install -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port that the FastAPI app will listen on
EXPOSE 8000

# Run the FastAPI app using Uvicorn when the container is started
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
