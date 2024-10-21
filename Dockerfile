FROM python:3.12-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd app
USER app

EXPOSE 8080
CMD ["bash", "./app.sh"]

