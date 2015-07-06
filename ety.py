#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='Lookup who sampled a song.')
parser.add_argument(
    'artist',
    type=str,
    nargs='+',
    help='The sampled artist.'
)
parser.add_argument(
    'song',
    type=str,
    nargs='+',
    help='The song.'
)
args = parser.parse_args()

def main():
    if args.song:
        q = args.song[0]
        response = requests.get('http://www.whosampled.com/search/?q={0}'.format(q))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for worddef in soup.find_all('a', {'class': 'trackName'}):
            print('')
            print(worddef.get_text().strip())
            print(worddef.find_next_sibling().get_text().strip())
    else:
        print('No query')

if __name__ == "__main__":
    main()