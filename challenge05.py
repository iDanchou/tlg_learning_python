#! /usr/bin/python3
heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

char_name = input('Which character do you want to know about? (Flash, Batman, or Superman)\n:')

print(f'The hero you chose was {char_name}!')

char_stat = input('Which stat are you the most curious about? (Strength, Speed, or Intelligence \n:')

print(f'The stat you chose is {char_stat}!')

while True:
    if char_name.lower() == 'flash' and char_stat.lower() == 'speed':
        print('Flash\'s speed is: ' + heroes['flash']['speed'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'flash' and char_stat.lower() == 'strength':
        print('Flash\'s strength is: ' + heroes['flash']['strength'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'flash' and char_stat.lower() == 'intelligence':
        print('Flash\'s intelligence is: ' + heroes['flash']['intelligence'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'batman' and char_stat.lower() == 'speed':
        print('Batman\'s speed is: ' + heroes['batman']['speed'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'batman' and char_stat.lower() == 'strength':
        print('Batman\'s strength is: ' + heroes['batman']['strength'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'batman' and char_stat.lower() == 'intelligence':
        print('Batman\'s intelligence is: ' + heroes['batman']['intelligence'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'superman' and char_stat.lower() == 'speed':
        print('Superman\'s speed is: ' + heroes['superman']['speed'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'superman' and char_stat.lower() == 'strength':
        print('Superman\'s speed is: ' + heroes['superman']['strength'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    elif char_name.lower() == 'superman' and char_stat.lower() == 'intelligence':
        print('Superman\'s speed is: ' + heroes['superman']['intelligence'])
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
    else:
        print('I don\'t understand the output. Please try again.')
        go = input('Would you like to learn more? Enter y or n')
        if go == 'y':
            continue
        else:
            break
