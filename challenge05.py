#! /usr/bin/python3
heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

char_name = input('Which character do you want to know about? (Flash, Batman, or Superman)\n:')

print(f'The hero you chose was {char_name}!')

char_stat = input('Which stat are you the most curious about? (Strength, Speed, or Intelligence \n:')

print(f'The stat you chose is {char_stat}!')

while True:
    if char_name == 'Flash' and char_stat == 'Speed':
        print('Flash\'s speed is: ' + heroes['flash']['speed'])
        break
    elif char_name == 'Flash' and char_stat == 'Strength':
        print('Flash\'s strength is: ' + heroes['flash']['strength'])
        break
    elif char_name == 'Flash' and char_stat == 'Intelligence':
        print('Flash\'s intelligence is: ' + heroes['flash']['intelligence'])
        break
    elif char_name == 'Batman' and char_stat == 'Speed':
        print('Batman\'s speed is: ' + heroes['batman']['speed'])
        break
    elif char_name == 'Batman' and char_stat == 'Strength':
        print('Batman\'s strength is: ' + heroes['batman']['strength'])
        break
    elif char_name == 'Batman' and char_stat == 'Intelligence':
        print('Batman\'s intelligence is: ' + heroes['batman']['intelligence']
        break
    elif char_name == 'Superman' and char_stat == 'Speed':
        print('Superman\'s speed is: ' + heroes['superman']['speed'])
        break
    elif char_name == 'Superman' and char_stat == 'Strength':
        print('Superman\'s speed is: ' + heroes['superman']['strength'])
        break
    elif char_name == 'Superman' and char_stat == 'Intelligence':
        print('Superman\'s speed is: ' + heroes['superman']['intelligence'])
        break
    else:
        print('I don\'t understand the output. Please try again.')
        break

