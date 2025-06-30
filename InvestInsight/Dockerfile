# Dockerfile

# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose the port
EXPOSE 8000

# Command
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
ENTRYPOINT ["sh", "/app/start.sh"]