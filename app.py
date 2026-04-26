from flask import Flask, render_template
import psutil
import platform
import socket
import time

app = Flask(__name__)

@app.route("/")
def dashboard():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time

    uptime = {
        "days": int(uptime_seconds // 86400),
        "hours": int((uptime_seconds % 86400) // 3600),
        "minutes": int((uptime_seconds % 3600) // 60)
    }

    stats = {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.release(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory(),
        "disk": psutil.disk_usage("/"),
        "process_count": len(psutil.pids()),
        "uptime": uptime
    }

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
