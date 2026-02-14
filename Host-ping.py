#!/usr/bin/env python3
"""
Multi-Host Ping Monitor
"""

import os
import platform
import time
from datetime import datetime

# ----------------------
ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]
log_file = "ping_log.txt"
interval = 10  

# OS detection for ping parameter
param = "-n" if platform.system().lower() == "windows" else "-c"

# ----------------------
try:
    while True:
        for ip in ips:
            ip = ip.strip()
            if not ip:
                continue

            # print command for debug
            print(f"Pinging {ip} ...")

            response = os.system(f"ping {param} 1 {ip}")

            status = "UP" if response == 0 else "DOWN"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{timestamp} | {ip} | {status}"

            print(line)

            # write to log
            with open(log_file, "a") as f:
                f.write(line + "\n")

        time.sleep(interval)
