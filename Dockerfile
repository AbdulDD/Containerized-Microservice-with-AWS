# Use a small, stable Python base
FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Copy only requirements first for build caching
COPY requirements.txt .

# Install dependencies (no pip cache to save space)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port the app listens on
EXPOSE 8080

# Default command to run the Flask app
CMD ["python", "main.py"]
