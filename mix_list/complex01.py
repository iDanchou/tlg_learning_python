#! /usr/bin/env python3

# create a list called list1
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']

# display list1
print(list1)

# print second item on list
print(list1[1])

# create a second list 
list2 = ['juniper']

# extend list1 by list2 (combine both together)
list1.extend(list2)

print(list1)

# create a third list
list3 = ['10.1.0.1', '10.2.0.1', '10.3.0.1']

# append list3 to list1

list1.append(list3)

print(list1)

# display the list of IP addresses
print(list1[4])

# display the first item on the list of IP addresses
print(list1[4][0])

# create a list of animals with three letter names
animals = ['pig', 'hen', 'cow', 'dog', 'koi', 'fox', 'bee']

print(animals)

animals.append('cat')

print(animals)
