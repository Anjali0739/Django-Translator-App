# -------------------------------
# Dockerfile: Django + Redis (single container)
# -------------------------------

FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Redis server and required system packages
RUN apt-get update && apt-get install -y \
    redis-server \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project files into container
COPY . .

# Expose both Django and Redis ports
EXPOSE 8000 6379

# Start Redis server and Django together
CMD redis-server --daemonize yes && python manage.py runserver 0.0.0.0:8000
