#! /usr/bin/env python3

print('Hello, let\'s convert your test percentage to a letter grade.')

# prompt user to input percentage
grade = int(input('Enter your numeric score: '))

# begin if-logic script
if grade > 100:
   print('This number is not valid on the grading scale')
elif grade >= 90:
    print('You have received an A!')
elif grade >= 80 and grade < 90:
    print('You have received a B!')
elif grade >= 70 and grade < 80:
    print('You have received a C.')
elif grade >= 60 and grade < 69:
    print('You have received a D.')
else:
    print('You have received an F.')
