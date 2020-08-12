import random

password = str(input("Enter password only numbers : "))

guess = " "

while guess != password:
    guess = str(random.randint(100000,999999))

    print("=> " + guess)

    if guess == password:
        print("The password is :" + password)
        break