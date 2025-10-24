# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create directory for database
RUN mkdir -p /app/data

# Expose port (Cloud Run will set PORT environment variable)
ENV PORT=8080
EXPOSE 8080

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 webapp:app
