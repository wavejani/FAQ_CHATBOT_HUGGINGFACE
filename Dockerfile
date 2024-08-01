# Use the official Python slim image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the source code and app files into the container
COPY src/ src/
COPY app.py app.py

# Set the command to run the application
CMD ["python", "app.py"]
