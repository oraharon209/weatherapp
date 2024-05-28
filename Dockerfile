FROM python:3.9-alpine

# Create a new user
RUN adduser --disabled-password oraharon

# Set the working directory
WORKDIR /weatherapp

# Copy the application code
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure gunicorn is installed globally
RUN pip install --no-cache-dir gunicorn

# Switch to the non-root user
USER oraharon

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:9090", "wsgi:app"]
