import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url: ')

# A função .read() lê a página inteira de uma vez, não em loop 
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Recuperar todos os links da página
# retorna lista com os links
tags = soup('a')
for tag in tags:
    print('Links recuperados: ', tag.get('href', None))


#num = [108,105,110,101]
#for n in num:
#    #print(ord(n))
#    print(chr(n))