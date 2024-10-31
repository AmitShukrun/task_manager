FROM python:3.9

# Ensure unbuffered output (useful for logging)
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Use gunicorn instead of Django's built-in server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
