#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# easy solution

for every_animal in farms[0]['agriculture']:
    print(every_animal)

choose_farm = input('Welcome to the farm! Please choose which location you\'re interested in viewing.\nNE Farm:\nW Farm:\nSE Farm:\n:')

# medium solution

if choose_farm.lower() == 'ne farm':
    for every_farm in farms[0]['agriculture']:
        print(every_farm)
elif choose_farm.lower() == 'w farm':
    for every_farm in farms[1]['agriculture']:
        print(every_farm)
elif choose_farm.lower() == 'se farm':
    for every_farm in farms[2]['agriculture']:
        print(every_farm)
else:
    print('That doesn\'t look like one of the options.')

# hard solution

choose_farm = input('Welcome to the farm! Please choose which location you\'re interested in viewing.\nNE Farm:\nW Farm:\nSE Farm:\n:')

if choose_farm.lower() == 'ne farm':
    for every_farm in farms[0]['agriculture']:
        print(every_farm)
elif choose_farm.lower() == 'w farm':
    for every_farm in farms[1]['agriculture']:
        print(every_farm)
elif choose_farm.lower() == 'se farm':
    print(farms[2]['agriculture'][0])
else:
    print('That doesn\'t look like one of the options.')

