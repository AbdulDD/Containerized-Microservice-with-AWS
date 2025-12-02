# Base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose Flask port
EXPOSE 5000

# Run Flask app (adjust path to utils/app.py)
CMD ["python", "app.py"]
