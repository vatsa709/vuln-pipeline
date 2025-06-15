import os
import time
import subprocess
from git import Repo

REPO_PATH = "../app/juice-shop"
repo = Repo(REPO_PATH)

def trigger_scan():
    print("[+] Starting vulnerability scan...")
    subprocess.run(["bash", "/home/kali/vuln-pipeline/scripts/scan_zap.sh"])

last_commit = None

while True:
    try:
        repo.remotes.origin.fetch()
        current_commit = repo.head.commit.hexsha

        if os.path.exists("pipeline.enabled") and current_commit != last_commit:
            print("[+] New Git push detected. Triggering vulnerability assessment pipeline...")
            last_commit = current_commit
            trigger_scan()
        else:
            print("[+] No new commits. Waiting...")
        time.sleep(30)
    except Exception as e:
        print(f"[!] Pipeline error: {str(e)}")
        time.sleep(30)
