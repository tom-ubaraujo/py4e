import urllib.request, urllib.parse, urllib.error
import json
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
data = urllib.request.urlopen(url, context=ctx).read().decode()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

count_sum = 0
for comment in js["comments"]:
    count_sum += int(comment["count"])

print("Count: ",len(js["comments"]))
print("Sum: ",count_sum)