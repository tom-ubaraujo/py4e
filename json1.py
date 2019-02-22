import json

data = '''
{
    "name" : "Tom",
    "phone": {
        "type" : "intl",
        "number" : "999999999"
        },
    "email": {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
print('Phone: ', info["phone"]["number"])