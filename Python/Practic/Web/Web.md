# Web
- HTTP - Hypertext transport protocol
- HTML - Hypertext markup language
- URL  - Uniform resource location
### Urllib library
```python
import urllib.request as ur

if __name__ == "__main__":
    url = 'http://www.example.com'
    conn = ur.urlopen(url)
    print(f'[INFO] Conn.status: {conn.status}')
    print(f'[INFO] data: {conn.read()}')
    for key, value in conn.getheaders():
        print(f'[INFO] key: {key}, value: {value}')
# Output:
# [INFO] key: Content-Type, value: text/html
# [INFO] key: ETag, value: "bc2473a18e003bdb249eba5ce893033f:1760028122.592274"
# [INFO] key: Last-Modified, value: Thu, 09 Oct 2025 16:42:02 GMT
# [INFO] key: Vary, value: Accept-Encoding
# [INFO] key: Cache-Control, value: max-age=86000
# [INFO] key: Date, value: Tue, 14 Oct 2025 14:58:36 GMT
# [INFO] key: Content-Length, value: 513
# [INFO] key: Connection, value: close
```
### Requests library
```python
import json
import sys
import requests

def search(title):
    url = 'https://archive.org/advancedseearch.php'
    params = {
        'q': f'title:({title})',
        'output': 'json',
        'fields': 'identifier,title',
        'rows': 50,
        'page': 1,
    }
    resp = requests.get(url, params=params)
    return resp.json()

if __name__ == "__main__":
    title = 'wendigo'
    data = search(title)
    docs = data['response']['docs']
    print(f'[INFO] Found {len(docs)} items, showing first 10')
    print(f'[INFO] identifier\ttitle')
    for row in docs[:10]:
        print(row['identifier'], row['title'], sep='\t')
```
### Web servers
We can run web server by using python
- $ python -m http.server

Through command: localhost:8000 we can get access to the file system of the server.
### Web Server Gateway Interface (WSGI)
### Bottle
#### Simplest example
```python
from bottle import route, run

@route('/')
def home():
    return "It isn't fancy, but it's my home page"

if __name__ == "__main__":
    run(host='localhost', port=8000)
```
#### Bottle with html files
```python
from bottle import route, run, static_file

@route('/')
def main():
    return static_file('./Sources/index.html', root='.')

if __name__ == "__main__":
    run(host='localhost', port=8000)
```
#### Bottle with additional functionality
```python
from bottle import route, run, static_file

@route('/')
def home():
    return static_file('./Sources/index.html', root='.')
@route('/echo/<thing>')
def echo(thing):
    return f"Say hello to my little friend: {thing}!"

if __name__ == "__main__":
    run(host='localhost', port=8000)
```
### Scrapy
```python
import requests
from bs4 import BeautifulSoup as soup
import sys

def get_links(url):
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == "__main__":
    all_links = ['http://boingboing.net']

    for url in all_links:
        print(f'[INFO] Link: {url}')
        for num, link in enumerate(get_links(url), start=1):
            print(f'[LINK] num: {num}, link: {link}')
        print('')
```