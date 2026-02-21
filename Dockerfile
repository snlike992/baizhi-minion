FROM python:3.9-slim
WORKDIR /app
COPY heartbeat.py .
CMD ["python", "-u", "heartbeat.py"]