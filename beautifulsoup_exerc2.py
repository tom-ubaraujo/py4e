import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('Enter URL: ')
repeat = int(input('Repet: '))
pos = int(input('Position: '))

i = 0
while i < repeat:
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    url = tags[pos-1].get('href', None)
    print(f'Nome {i+1}: ', tags[pos-1].contents[0])

    i += 1