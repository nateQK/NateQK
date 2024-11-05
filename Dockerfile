FROM python:3.12-slim

COPY . /app
WORKDIR /app


# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	gcc \
	python3-dev \
	&& rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

RUN useradd app
USER app

EXPOSE 8080
CMD ["bash", "./app.sh"]

