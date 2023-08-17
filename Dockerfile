# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y wget unzip

# Download and install ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE
RUN unzip /tmp/chromedriver.zip -d /opt/render/Routine-Maker
RUN chmod +x /opt/render/Routine-Maker/chromedriver

# Copy the requirements file into the container at /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for FastAPI to run on
ENV PORT=80

# Run FastAPI app when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
