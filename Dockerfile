# Use official Python lightweight image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 82

# Run FastAPI application (set module path explicitly)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "82", "--reload"]
