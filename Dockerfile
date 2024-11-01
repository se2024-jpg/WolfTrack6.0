FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*  # Clean up APT when done

# Set the working directory
WORKDIR /app

# Copy only requirements.txt to leverage Docker cache
COPY ./requirements.txt .

# Upgrade pip and install dependencies
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the entrypoint
ENTRYPOINT ["python3", "main.py"]
