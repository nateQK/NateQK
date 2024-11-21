FROM python:3.13-alpine

# Copy application files
COPY . /app
WORKDIR /app

# Install build dependencies and Inkscape
RUN apk add --no-cache \
	gcc \
	musl-dev \
	python3-dev \
	linux-headers

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN adduser -D app
USER app

# Expose application port
EXPOSE 8080

# Command to run the application
CMD ["bash", "/app/run.sh"]

