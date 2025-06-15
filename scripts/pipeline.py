#!/usr/bin/env python3

import os
import sys
import subprocess

PID_FILE = "pipeline.pid"
ENABLED_FLAG = "pipeline.enabled"

def start_pipeline():
    if os.path.exists(PID_FILE):
        print("Pipeline already running.")
        return

    with open(ENABLED_FLAG, 'w') as f:
        f.write("enabled")

    proc = subprocess.Popen(["python3", "git_monitor.py"])
    with open(PID_FILE, 'w') as f:
        f.write(str(proc.pid))

    print("Pipeline started.")

def stop_pipeline():
    if not os.path.exists(PID_FILE):
        print("Pipeline not running.")
        return

    with open(PID_FILE, 'r') as f:
        pid = int(f.read())
    try:
        os.kill(pid, 9)
        print("Pipeline stopped.")
    except ProcessLookupError:
        print("Process already terminated.")
    os.remove(PID_FILE)

    if os.path.exists(ENABLED_FLAG):
        os.remove(ENABLED_FLAG)

def status_pipeline():
    if os.path.exists(PID_FILE):
        print("Pipeline is running.")
    else:
        print("Pipeline is not running.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pipeline.py start|stop|status")
        sys.exit(1)

    if sys.argv[1] == "start":
        start_pipeline()
    elif sys.argv[1] == "stop":
        stop_pipeline()
    elif sys.argv[1] == "status":
        status_pipeline()
    else:
        print("Unknown command")
