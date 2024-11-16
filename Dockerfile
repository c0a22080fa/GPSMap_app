# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
