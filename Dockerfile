# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .


# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn


# Expose the port your app will run on
EXPOSE 8000

# Command to run the application
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:8000"]
