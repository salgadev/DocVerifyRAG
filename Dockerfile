# Use an official Python runtime as a parent image
FROM python:3.9-slim AS backend

# Set the working directory for the backend in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
        && apt-get install -y --no-install-recommends gcc \
        && rm -rf /var/lib/apt/lists/*

# Copy backend application dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend source code from the root directory
COPY . /app/

# Expose the port the backend app runs on
EXPOSE 5000

# Build frontend
FROM node:14 AS frontend

# Set the working directory for the frontend in the container
WORKDIR /app/frontend

# Copy frontend source code
COPY frontend /app/frontend

# Install frontend dependencies and build
RUN npm install
RUN npm run build

# Merge frontend build with backend
FROM backend AS final

# Copy built frontend files to appropriate location for serving
COPY --from=frontend /app/frontend/dist /app/frontend/dist

# Add configuration to serve frontend files using Nginx
# Example:
# COPY nginx.conf /etc/nginx/nginx.conf

# Start the backend server
CMD ["python", "together_call.py"]

