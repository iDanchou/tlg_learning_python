import requests

r = requests.get('http://api.open-notify.org/astros.json')

#astros= {"number": 3, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}], "message": "success"}

astros = r.json()
print("People in space: ", astros["number"])

for x in astros["people"]:
    print(f"{x['name']} is on the {x['craft']}")
