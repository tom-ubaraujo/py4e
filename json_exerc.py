import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
    print("Invalid URL!")
    exit()

# address and API_Key to be added at the end of the url
parms = dict()
parms['address'] = address
parms['key'] = 42

# encode the parms with the url, to access the API
url = serviceurl + urllib.parse.urlencode(parms)
data = urllib.request.urlopen(url, context=ctx).read().decode()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

# saving the returned data into the variable js, which is a dict()
try:
    js = json.loads(data)
except:
    js = None

# testing for error in the process of retrieving data
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

placeid = ""
placeid = js['results'][0]['place_id']
print("Place id: ",placeid)