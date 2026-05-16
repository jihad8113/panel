import subprocess
import sys
import time
#------------------------------------#
scripts = [


    "d3.1.ims[ENC].py",
    "green_sohag[ENC].py", 
    "number_panel_api[ENC].py",
   # "7onetel[ENC].py",  
    "pscall[ENC].py",
    "zonesms2[ENC].py",  
    "mongodb_hn_data[ENC].py",
    "kz[ENC].py"
   # "seven_one_tel[ENC].p
 
    
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