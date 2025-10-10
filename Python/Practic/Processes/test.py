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