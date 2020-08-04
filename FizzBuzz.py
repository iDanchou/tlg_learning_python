fizz = 0
buzz = 0
fizzbuzz = 0
integers = 0

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
        fizzbuzz += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz += 1
    else:
        print(i)
        integers += 1

print('\n')
print("Fizz = " ,fizz)
print("Buzz = ", buzz)
print("FizzBuzz = ", fizzbuzz)
print("Integers = ", integers)