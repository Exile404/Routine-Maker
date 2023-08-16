# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for FastAPI to run in production mode
ENV FASTAPI_ENV=production

# Run the FastAPI app using Gunicorn when the container launches
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80", "--workers", "4"]
