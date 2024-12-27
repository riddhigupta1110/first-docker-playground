# Use a Python base image
FROM python:3.11-slim

# Set environment variables to avoid buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Copy the rest of the application code to the container
COPY . /app/

# Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait-for-it script
COPY scripts/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expose the port the app will run on
EXPOSE 5000

CMD ["/wait-for-it.sh", "mysql","3306", "--", "python", "app.py"] 
