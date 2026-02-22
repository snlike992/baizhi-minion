FROM python:3.11-slim
WORKDIR /app
# 移除旧的 heartbeat 脚本
COPY minion_harvester.py .
# 环境变量预设
ENV PYTHONUNBUFFERED=1
CMD ["python", "minion_harvester.py"]
