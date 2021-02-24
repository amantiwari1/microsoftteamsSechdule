import time
import subprocess

p = subprocess.Popen(["cat"])
time.sleep(10) #delay of 10 seconds
p.kill()
