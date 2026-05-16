import subprocess
import sys
import time
#------------------------------------#
scripts = [
    "timesms_sohag[ENC].py"
  #  "seven_one_tel[ENC].py"
]
#------------------------------------#
processes = []
def start(script):
    print(f"Starting {script} ...")
    return subprocess.Popen([sys.executable, script])
for script in scripts:
    processes.append(start(script))
while True:
    for i, p in enumerate(processes):
        if p.poll() is not None:  # process stopped
            print(f"{scripts[i]} crashed. restarting...")
            processes[i] = start(scripts[i])
    time.sleep(5)
