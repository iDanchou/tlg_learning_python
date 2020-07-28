#! /usr/bin/python3

def numVowels(string):
    string = string.lower() # lowercase the strings
    count = 0 # keeps track of all the vowels
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'e' or \
                string[i] == 'i' or string[i] == 'o' \
                or string[i] == 'u':
                    count += 1
    return count

str = input('Enter your string: ')
print('{} has {} vowels.'.format(str, numVowels(str)))
