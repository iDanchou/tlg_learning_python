#! /usr/bin/env python3

import random

guesses = 0

print('Hello! Enter your name.')
name = input()

secret = random.randint(1,100)
print(name + 'I have a number 1-100.')

while guesses < 9999:
    print('Take your best guess!')
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < secret:
        print(guess,  'is too low!')

    if guess > secret:
        print(guess, 'is too high!')

    if guess == secret:
        break
if guess == secret:
    print(name, ',', guess, 'was right! You got it!')

