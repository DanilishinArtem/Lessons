# Processes
## Process is isolated out of other processes, process can't see what other processes are doing!

Table 1. Basic functions
|Function|Return|
|--------|------|
|os.getpid|pid of the process|
|os.getcwd|current working directory|
|os.getuid|id of the user|
|os.getgid|id of the group|

## Creation of the process
```python
import subprocess

if __name__ == "__main__":
    ret = subprocess.getoutput('date')
    print(f'[INFO] ret: {ret}')
    ret = subprocess.check_output('date')
    print(f'[INFO] ret: {ret}')
    ret = subprocess.getstatusoutput('date')
    print(f'[INFO] ret: {ret}')
    ret = subprocess.call('date')
    print(f'[INFO] ret: {ret}')
# ---------- output ----------
# [INFO] ret: Sat Oct 11 00:35:11 MSK 2025
# [INFO] ret: b'Sat Oct 11 00:35:11 MSK 2025\n'
# [INFO] ret: (0, 'Sat Oct 11 00:35:11 MSK 2025')
# Sat Oct 11 00:35:11 MSK 2025
# [INFO] ret: 0
```
## Creation of the process by using multiprocessing
```python
import multiprocessing
import os

def whoami(what):
    print(f'[INFO] Process {os.getpid()} says: {what}')

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(
            target=whoami,
            args=(f"I'm function {n}",)
        )
        p.start()
# ---------- output ----------
# [INFO] Process 29678 says: I'm the main program
# [INFO] Process 29681 says: I'm function 0
# [INFO] Process 29682 says: I'm function 1
# [INFO] Process 29683 says: I'm function 2
# [INFO] Process 29684 says: I'm function 3
```
## Killing process by using terminate
```python
import multiprocessing
import time
import os

def whoami(what):
    print(f'[INFO] Process {os.getpid()} says: {what}')

def loopy(name):
    whoami(name)
    start = 1
    stop = 1_000_000
    for num in range(start, stop):
        print(f'[INFO] Number {num} of {stop}. Honk!')
        time.sleep(1)

if __name__ == "__main__":
    whoami('main')
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
# ---------- output ----------
# [INFO] Process 32206 says: main
# [INFO] Process 32208 says: loopy
# [INFO] Number 1 of 1000000. Honk!
# [INFO] Number 2 of 1000000. Honk!
# [INFO] Number 3 of 1000000. Honk!
# [INFO] Number 4 of 1000000. Honk!
# [INFO] Number 5 of 1000000. Honk!
```
# Concurrency
<!-- 310 -->