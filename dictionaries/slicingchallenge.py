#! /usr/bin/python3

easy = ['science', 'turbo', ['goggles', 'eyes'], 'nothing']

medium = ['science', 'turbo', {'eyes': 'goggles', 'goggles': 'eyes'}, 'nothing']

hard = [{'slappy': 'a', 'text': 'b', 'kumquat': 'goggles', 'user':{'awesome': 'c', 'name': {'first': 'eyes', 'last': 'toes'}}, 'banana': 15, 'd': 'nothing'}]

print(f'My {easy[2][1]}! The {easy[2][0]} do {easy[3]}!'}) 
