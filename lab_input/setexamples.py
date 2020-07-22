#! /usr/bin/env python3

s = {1, 1, 1, 2, 1, 4, 5, 10, 9, 9}  # only contain unique elements
print(s)

x = [1, 1, 1, 2, 1, 2, 3, 3, 5, 2, 1]
z = list(set(x))
print(z)

a, b = {1, 2, 1}, {1, 1, 3, 4}
c = a.intersection(b)
d = a.union(b)
print(c)
print(d)

print(a & b)  # same thing as intersection, shorthand notation
print(a | b)  # same thing as union, shorthand notation
