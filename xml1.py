import xml.etree.ElementTree as ET 

data =  '''<person>
            <name>Chuck</name>
            <phone type="intl">+1 734 303 4456</phone>
            <email hide="yes">ugleiston@gmail.com</email>
        </person>'''

tree = ET.fromstring(data)

print('Name: ',tree.find('name').text)
print('Attr: ',tree.find('email').get('hide'))
print('Phone: ',tree.find('email').text)
 