# range(x, y, z)

# x = number you begin counting from

# y = number you count UP( or down) just short of...this number will not be included in the range!

# z = the increment you/'ll move by- 1 goes up by one, -2 goes down by two.

for x in range(10):  # counting up from 0 to 9
    print(x, end=' ')

print('\n')  # skipping line for readability

for x in range(4, 32, 2):  # counting up from 4 to 30 by even numbers (including 30)
    print(x, end=' ')

print('\n')  # skipping line for readability

beer = int(input('> '))  # collecting input for beer


if beer > 100:
    print("Sorry, that value is too high! We can't be here forever!")
else:
    for x in range(beer, 0, -1):
        print(f"""{x} bottles of beer on the wall!
    {x} bottles of beer! Take one down, pass it around!
    {x - 1} bottles of beer on the wall!""")
