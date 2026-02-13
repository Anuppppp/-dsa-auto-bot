# use officil python slim image
FROM python:3.11-slim

# Set working directory insider container
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
Copy . .

# default command
CMD ["python", "-m", "orchestrator.bot"]