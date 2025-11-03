# Bruteforce folders of the web resource
### Code for bruteforce of folders by using dict consisted in the txt file
```python
import queue
import requests
import threading
import sys

AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
TARGET = "http://testphp.vulnweb.com"
THREADS = 1
WORDLIST = "/Users/adanilishin/Lessons/Python_2_greyhat/Web/Sources/all.txt"

def get_words(resume=None):
    def extend_words(word):
        if "." in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')
        
        for extension in EXTENSIONS:
            words.put(f'/{word}{extension}')

    with open(WORDLIST) as f:
        raw_words = f.read()

    found_resume = False
    words = queue.Queue()
    for word in raw_words.split():
        if resume is not None:
            if found_resume:
                extend_words(word)
            elif word == resume:
                found_resume = True
                print(f'Resuming wordlist from : {resume}')
        else:
            print(word)
            extend_words(word)
    return words


def dir_bruter(words):
    headers = {'User-Agent': AGENT}
    while not words.empty():
        url = f'{TARGET}{words.get()}'
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            sys.stderr.write('x')
            sys.stderr.flush()
            continue
        if r.status_code == 200:
            print(f'\nSuccess ({r.status_code}: {url})')
        elif r.status_code == 404:
            sys.stderr.write('.')
            sys.stderr.flush()
        else:
            print(f'{r.status_code} => {url}')


if __name__ == "__main__":
    words = get_words()
    print('Press return to continue.')
    sys.stdin.readline()
    for _ in range(THREADS):
        t = threading.Thread(target=dir_bruter, args=(words,))
        t.start()
# Constructed list for bruteforce attack (base: CSV)
# INFO:root:/CSV/
# INFO:root:/CSV.php
# INFO:root:/CSV.bak
# INFO:root:/CSV.orig
# INFO:root:/CSV.inc
# INFO:root:/admin/
# INFO:root:/admin.php
```
### Output for script:
```python
# .....
# Success (200: http://testphp.vulnweb.com/admin/)
# .....
# Success (200: http://testphp.vulnweb.com/index.php)

# Success (200: http://testphp.vulnweb.com/index.bak)
# ...
# Success (200: http://testphp.vulnweb.com/search.php)
```
### Hacking HTML form, authentification by using bruteforce method
