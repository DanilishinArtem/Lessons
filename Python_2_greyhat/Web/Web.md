# Web
## Remark (about generators)
### The first example
```python
def my_generator(n):
    while n > 0:
        yield n
        n -=1

if __name__ == "__main__":
    gen = my_generator(10)
    for i in gen:
        print(i)
```
### Sending values into the generator
```python
def my_generator():
    while True:
        value = yield
        print(f'Got value: {value}')

if __name__ == "__main__":
    gen = my_generator()
    # gen.send('the first') ---> not valid row
    # run generator until the first yield
    next(gen)
    gen.send('Hello')
    gen.send('world')
```
### working with directories with the controle of the finall directory
```python
@contextlib.contextmanager
def chdir(path):
    # save the frist directory
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        # restore the first directory
        os.chdir(this_dir)

if __name__ == "__main__":
    with chdir('some/dir/which/we/are/working/'):
        foo()
```
### try/finally
```python
try:
    something_that_might_cause_an_error()
except SomeError as e:
    print(e)             # print an error
    do somethingelse()   # do some althernative action
else:
    everything_is_fine() # do if we have success
finally:
    cleanup()            # do it in any case
```
### contextlib.contextmanager
```python
class TestClass:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print('[INFO] enter method')

    def __exit__(self, exc_type, exc_value, traceback):
        print('[INFO] exit method')

    def print(self):
        print(f'Hello, {self.name}')


if __name__ == "__main__":
    test = Test('Artem')
    with test:
        test.print()
# Output:
# [INFO] enter method
# Hello, Artem
# [INFO] exit method
```
### Urllib library
```python
# GET method
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = 'http://google.com'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(content)
```
```python
# POST method
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = "https://api.mindbox.ru/v3/js/operations/async?"
    info = {
        'version':'1.0.738',
        'transport':'beacon',
        'operation':'popmechanic-popup-123075-targeting',
        'originDomain':'usmall.ru',
        'trackerName':'mindbox'
    }
    data = urllib.parse.urlencode(info).encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content)
```
### Requests library
```python
# GET method
import requests

if __name__ == "__main__":
    url = 'http://google.com'
    response = requests.get(url)
    print(response.content)
```
```python
# POST method
import requests

if __name__ == "__main__":
    url = "https://api.mindbox.ru/v3/js/operations/async?"
    data = {
        'version':'1.0.738',
        'transport':'beacon',
        'operation':'popmechanic-popup-123075-targeting',
        'originDomain':'usmall.ru',
        'trackerName':'mindbox'
    }
    response = requests.post(url, data=data)
    print(response.text)
```
### Packages lxml and BeautifulSoup
#### lxml
```python
from io import BytesIO
from lxml import etree

import requests

if __name__ == "__main__":
    url = 'https://nostarch.com'
    r = requests.get(url)
    content = r.content
    parser = etree.HTMLParser()
    content = etree.parse(BytesIO(content), parser=parser) # convert to tree
    for link in content.findall('//a'):
        print(f"{link.get('href')} -> {link.text}")
```
#### beautifulSoup
```python
from bs4 import BeautifulSoup as bs
import requests


if __name__ == "__main__":
    url = 'http://bing.com'
    r = requests.get(url)
    tree = bs(r.text, 'html.parser') # convert to the tree
    for link in tree.find_all('a'): # find all links (elements 'a')
        print(f"{link.get('href')} -> {link.text}")
```
### Example of exploring inside the directory
```python
import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERED = [".jpg", ".gif", ".png", ".css"]
# TARGET = "http://boodelyboo.com/wordpress"
TARGET = "http://mail.ru"
THREADS = 1

answers = queue.Queue()
web_paths = queue.Queue()

def gather_paths(info: bool = False):
    for root, _, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            if info:
                print(path)
            web_paths.put(path)


@contextlib.contextmanager
def chdir(path):
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)


def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        time.sleep(2)
        r = requests.get(url)
        if r.status_code == 200:
            answers.put(url)
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')
        sys.stdout.flush()


def run():
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()

    for thread in mythreads:
        thread.join()


if __name__ == "__main__":
    with chdir("/Users/adanilishin/Lessons/Python_2_greyhat/Web/Sources/wordpress"):
        gather_paths(False)
    input("Press return to continue.")

    run()
    with open('myanswers.txt', 'w') as f:
        while not answers.empty():
            f.write(f'{answers.get()}\n')
    print('Done')
# Output:
# Press return to continue.
# Spawning thread 0
# Spawning thread 1
# Spawning thread 2
# Spawning thread 3
# Spawning thread 4
# Spawning thread 5
# Spawning thread 6
# Spawning thread 7
# Spawning thread 8
# Spawning thread 9
# ++++++++++xxxxxxxxxxxxxxxx
```