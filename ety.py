#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='Lookup the etymology of a word.')
parser.add_argument(
    'word',
    type=str,
    nargs='+',
    help='The word you wish to etymologize.'
)
args = parser.parse_args()

def main():
    if args.word:
        q = args.word[0]
        response = requests.get('http://www.etymonline.com/index.php?term={0}'.format(q))
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        for worddef in soup.find_all('dt'):
            print('')
            print(worddef.get_text().strip())
            print(worddef.find_next_sibling().get_text().strip())
    else:
        print('No query')

if __name__ == "__main__":
    main()