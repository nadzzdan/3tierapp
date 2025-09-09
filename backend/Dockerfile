# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run backend app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
