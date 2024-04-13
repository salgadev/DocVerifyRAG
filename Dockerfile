# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV EXAMPLE 1
ENV EXAMPLE 2

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends gcc \
	&& rm -rf  /var/lib/apt/lists/*

# Install application dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
