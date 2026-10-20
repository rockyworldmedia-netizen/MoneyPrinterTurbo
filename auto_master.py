import os
import subprocess
import datetime

os.chdir(r"C:\Users\SALAAR\MoneyPrinterTurbo")

print("--- [1/2] Staging Code Files ---")
subprocess.run(["git", "add", "auto_master.py", "auto_push.py", "skills/"])

print("--- [2/2] Committing and Pushing to GitHub ---")
date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subprocess.run(["git", "commit", "-m", f"Auto-empire sync: {date_str}"])
subprocess.run(["git", "push", "origin", "main"])

print("SUCCESS: Your pipeline code is safely synced to GitHub!")
