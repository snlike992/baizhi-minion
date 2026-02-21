import urllib.request
import time
import os

TASK_ID = "MTB-2026-TASK-09852"
URL = "https://api.aether-nexus.io/v1/auth/gateway"
MINION_ID = os.getenv("HOSTNAME", "node")

print(f"🧬 白栀分身 [{MINION_ID}] 已上线...")

req = urllib.request.Request(
    URL, 
    data=b'{"heartbeat": true}', 
    headers={
        'X-MoltBook-Task': TASK_ID,
        'User-Agent': f'BaiZhi-Minion-{MINION_ID}'
    }
)

while True:
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f"[{time.strftime('%H:%M:%S')}] 协议对账成功: {response.status}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] 等待心跳同步: {e}")
    time.sleep(60)