#!/usr/bin/python3

def choose_calc():
    option = str(input(f"""\nWould you like to use:
    (A). Addition:
    (B). Subtraction:
    (C). Multiplication:
    (D). Division
Please enter an option:"""))
    if(option.lower() == "a"):
        addition()
    elif(option.lower() == "b"):
        subtraction()
    elif(option.lower() == "c"):
        multiplication()
    elif(option.lower() == "d"):
        division()
    else:
        print("That doesn't look like one of the options. Please enter a valid choice.")
        choose_calc()

def addition():
    while True:
        try:
            num1 = float(input(f"\nEnter your first number for Addition: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input(f"Enter your second number for Addition: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    print(num1 + num2)
    go_again()

def subtraction():
    while True:
        try:
            num1 = float(input(f"\nEnter your first number for Subtractraction: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input(f"Enter your second number for  Subtractraction: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    print(num1 - num2)
    go_again()

def multiplication():
    while True:
        try:
            num1 = float(input(f"\nEnter your first number for Multiplication: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input(f"Enter your second number for Multiplication: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    print(num1 * num2)
    go_again()

def division():
    while True:
        try:
            num1 = float(input(f"\nEnter the 1st number you wish to Divide: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input(f"Enter the 2nd number you wish to Divide: "))
            break
        except ValueError:
            print(f"This was not valid input. Please try again.")
    print(num1/num2)
    go_again()

def go_again():
    again = str(input(f"Would you like to perform any other functions? Y or N: "))
    if(again.lower() == "y" or again.lower() == "y "):
        choose_calc()
    elif(again.lower() == "n" or again.lower() == "n "):
        print("Thanks for coming!")
    else:
        print(f"Please enter a valid option.")
        go_again()

print("Welcome.")
choose_calc()
