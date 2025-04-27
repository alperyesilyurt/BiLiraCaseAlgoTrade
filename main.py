import asyncio
from fastapi import FastAPI, Response
from datetime import datetime
import psutil
import time

from app.streamer import listen_to_orderbook

app = FastAPI()
start_time = time.time()

@app.on_event("startup")
async def startup_event():
    print("[Main] Starting orderbook listener...")
    asyncio.create_task(listen_to_orderbook())

@app.get("/health")
async def health_check():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

@app.get("/metrics")
async def metrics_prometheus_format():
    uptime = time.time() - start_time
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0.5)

    metrics = (
        f"# HELP uptime_seconds System uptime in seconds\n"
        f"# TYPE uptime_seconds gauge\n"
        f"uptime_seconds {round(uptime, 2)}\n\n"
        f"# HELP cpu_percent CPU usage percentage\n"
        f"# TYPE cpu_percent gauge\n"
        f"cpu_percent {cpu}\n\n"
        f"# HELP memory_percent Memory usage percentage\n"
        f"# TYPE memory_percent gauge\n"
        f"memory_percent {memory.percent}\n\n"
        f"# HELP total_memory_mb Total system memory in MB\n"
        f"# TYPE total_memory_mb gauge\n"
        f"total_memory_mb {round(memory.total / 1024**2, 2)}\n\n"
        f"# HELP used_memory_mb Used system memory in MB\n"
        f"# TYPE used_memory_mb gauge\n"
        f"used_memory_mb {round(memory.used / 1024**2, 2)}\n"
    )

    return Response(content=metrics, media_type="text/plain")
