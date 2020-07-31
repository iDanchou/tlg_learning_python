#!/usr/bin/python3
import random

num = input("How many Shakespearean insults would you like? ")

insult_list = open("/home/captain/tlg_learning_python/insults.txt", "r")

def insult_generator(num):
    print("You are a", end="")
    for x in num:
      print(random.choice(insult_list))

insult_generator(num)
