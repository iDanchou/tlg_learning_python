#!/usr/bin/python3

astro = {"message": "success", "number": 5, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}, {"craft": "ISS", "name": "Doug Hurley"}, {"craft": "ISS", "name": "Bob Behnken"}]}

# write line that outputs how many people are aboard the ISS
x = 'People in space'
print(astro['number'])

for x in astro['people']:
    print(x['craft'])
    print(x['name'])

for x in astro['people']:
    print(f"{x['name']} is on the {x['craft']}")
