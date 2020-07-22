#! /usr/bin/env python3

integers = [1, 2, 4, 5, 10]  # a list of integers
print(integers)
integers.append(100)        # adds 100 to end of list
print(integers)
integers.append(6)          # adds 6 to end of list
print(integers)

integers.pop()              # renmoves 6 from the list
print(integers)

random_nums = [2, 4, 1, 6, 10, 3, 0]
random_nums.reverse()
print(random_nums)
random_nums.reverse()
print(random_nums)
random_nums.sort()
print(random_nums)
