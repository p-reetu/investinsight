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

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

# Expose the port
EXPOSE 8000

# Command
CMD ["gunicorn", "InvestInsight.wsgi:application", "--bind", "0.0.0.0:8000"]