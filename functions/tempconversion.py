#! /usr/bin/python3

# convert temperatures
# convert to farenheit
# convert to celsius

def fartocel(temp):
    return (temp - 32) * (5.0 / 9.0)

def celtofar(temp):
    return temp * (9.0 / 5.0) + 32.0

def convert(temp, toScale):
    if toScale.lower() == 'c' or toScale.lower() == 'celsius':
        return celtofar(temp)
    else:
        return fartocel(temp)

if __name__ == '__main__':
    temp = float(input('Enter in a temperature'))
    degrees = input('Enter in 'c' for Celsius or 'f' for Farenheit ')
    cel = convert(90, 'c')
    print(cel)
