#!/usr/local/bin/python3

from bs4 import BeautifulSoup
from urllib import request
import sys

if(len(sys.argv) > 1):

    q = sys.argv[1]

    with request.urlopen('http://www.etymonline.com/index.php?term='+q) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        for worddef in soup.find_all('dt'):
            print("")
            print(worddef.get_text())
            print(worddef.find_next_sibling().get_text())
else:
    print('No query')





