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
### We have a problem: one washer and several dryers
#### [1] Solution by using processes:
```python
import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print(f'[INFO] Washing {dish} dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print(f'[INFO] Drying {dish} dish')
        input.task_done()

if __name__ == "__main__":
    # Queue for interprocessing message passing
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()
```
#### [2] Solution by using threading:
```python
import threading, queue
import time

def washer(dishes, output):
    for dish in dishes:
        print(f'[INFO] Washing {dish} dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print(f'[INFO] Drying {dish} dish')
        input.task_done()

if __name__ == "__main__":
    # Queue for interprocessing message passing
    dish_queue = queue.Queue()
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()
```
### Library futures
This library can be used for both: threads and processes creation and using them. 
Example (This is example just demonstraiting possibility of using threads and processes in one library):
```python
from concurrent import futures
import time
import math

def calc(value):
    time.sleep(1)
    result = math.sqrt(value)
    return result

def use_threads(num, values):
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as tex:
        results = tex.map(calc, values)
    t2 = time.time()
    return t2 - t1

def use_processes(num, values):
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as pex:
        results = pex.map(calc, values)
    t2 = time.time()
    return t2 - t1

def main(workers, values):
    print(f'[INFO] Using {workers} workers for {len(values)} values')
    t_sec = use_threads(workers, values)
    print(f'[INFO] Threads took {t_sec} sec.')
    t_sec = use_processes(workers, values)
    print(f'[INFO] Processes took {t_sec} sec.')

if __name__ == "__main__":
    workers = 50
    values = list(range(1,51))
    main(workers, values)
# Output:
# [INFO] Using 50 workers for 50 values
# [INFO] Threads took 1.0086908340454102 sec.
# [INFO] Processes took 1.9904210567474365 sec.
```
Example (This is example demonstrate possibility of using in real task, reak numbers returned in the progress of calculation, if result is ready for some worker, we can get result):
```python
from concurrent import futures
import time
import math

def calc(value):
    time.sleep(1)
    result = math.sqrt(value)
    return result

def use_threads(num, values):
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as tex:
        tasks = [tex.submit(calc, value) for value in values]
        for f in futures.as_completed(tasks):
            yield f.result()

def use_processes(num, values):
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as pex:
        tasks = [pex.submit(calc, value) for value in values]
        for f in futures.as_completed(tasks):
            yield f.result()

def main(workers, values):
    print(f'[INFO] Using {workers} workers for {len(values)} values')
    print(f'[INFO] Result for theads using:')
    for index, result in enumerate(use_threads(workers, values)):
        print(f'Square root for value {values[index]} = {result}')
    print(f'[INFO] Result for processes using:')
    for index, result in enumerate(use_processes(workers, values)):
        print(f'Square root for value {values[index]} = {result}')

if __name__ == "__main__":
    workers = 5
    values = list(range(1,6))
    main(workers, values)

# Output:
# [INFO] Using 5 workers for 5 values
# [INFO] Result for theads using:
# Square root for value 1 = 1.0
# Square root for value 2 = 1.7320508075688772
# Square root for value 3 = 2.0
# Square root for value 4 = 1.4142135623730951
# Square root for value 5 = 2.23606797749979
# [INFO] Result for processes using:
# Square root for value 1 = 1.0
# Square root for value 2 = 1.4142135623730951
# Square root for value 3 = 1.7320508075688772
# Square root for value 4 = 2.0
# Square root for value 5 = 2.23606797749979
```