# Use an official Python runtime as the base image
FROM python:3.9-slim

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

# Run the FastAPI app when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
