# Stage 1: Build the Vite/Svelte static files
FROM node:16 AS builder

# Set working directory
WORKDIR /app/client

# Copy the package.json and package-lock.json files
COPY client/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the client source code
COPY client/ .

# Build the Vite/Svelte project
RUN npm run build

# Stage 2: Build the FastAPI application
FROM python:3.10

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI source code
COPY . .

# Copy the .env file
COPY .env .

# Copy the built static files from the previous stage
COPY --from=builder /app/client/dist ./client/dist

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
