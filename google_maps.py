import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    adress = input("Inform the location: ")
    if len(adress) < 1: 
        break

    url = serviceurl + urllib.parse.urlencode({'adress': adress})

    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print('lat ', lat, ' lng ', lng)
    location = js['results'][0]['formatted_address']

    print(location)