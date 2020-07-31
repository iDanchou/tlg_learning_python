#!/usr/bin/env python3
## create file object in "r"ead mode
count = 0
filename = input('Enter your file name:' )

with open(f"{filename}", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    for lines in configlist:
        linenumbers = configfile.write()
        count += 1
        print(count)

## file was just auto closed (no more indenting)

## display list with no "\n"
print(configlist)

