import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
nums = []

for tag in tags:
    nums.append(int(tag.contents[0]))

print('Count: ',sum(nums))