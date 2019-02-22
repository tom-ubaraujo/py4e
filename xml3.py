import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Receiving the url from user.
url = input("Enter location: ")
if len(url) < 1:
    print("Invalid URL!")
    exit()

# parsing the url to open the page and reading all its content
data = urllib.request.urlopen(url, context=ctx).read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
# list with all the tags 'comment' from page
results = tree.findall('comments/comment')

count_sum = 0
for item in results:
    count_sum += int(item.find('count').text)

print("Count: ",len(results))
print("Sum: ",count_sum)

