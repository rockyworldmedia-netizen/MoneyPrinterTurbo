import os
import subprocess
import datetime

os.chdir(r"C:\Users\SALAAR\MoneyPrinterTurbo")
subprocess.run(["git", "add", "storage/tasks/"])
subprocess.run(["git", "add", "skills/"])
date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subprocess.run(["git", "commit", "-m", f"Auto-empire video build and sync: {date_str}"])
subprocess.run(["git", "push", "origin", "main"])
print("Successfully synced your automated pipeline files to GitHub!")
