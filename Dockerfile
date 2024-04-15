# Use node image as a base for building frontend
FROM node:14 AS frontend

# Set the working directory for the frontend in the container
WORKDIR /app/frontend

# Copy frontend source code
COPY frontend /app/frontend

# Install frontend dependencies
RUN npm install

# Build the frontend for production
RUN npm run build

# Use nginx image to serve the built frontend
FROM nginx:alpine AS production

# Copy the built frontend from the previous stage to nginx
COPY --from=frontend /app/frontend/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]

