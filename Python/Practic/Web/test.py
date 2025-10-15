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