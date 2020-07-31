#!/usr/bin/python3

## sudo apt-install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def get_ip_data():
    input_ip = input('What is the IP address? ')
    input_driver = input('What is the driver associated with this device? ')
    input_date = input('What is the date? ')
    input_owner = input('Who is the owner? ')
    d = {'IP': input_ip, 'driver': input_driver, 'date': input_date, 'owner': input_owner}
    return d

# Runtime
mylistdict = []

print('Hello! This program will make you a *.xls file')

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break
filename = input('\nWhat is the name of the *.xls file? ')

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print('The file ' + filename + '.xls should be in your local directory')
