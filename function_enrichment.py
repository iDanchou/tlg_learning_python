# Part 1
def good_day():
    x= float(input("""How would you rank your day today on a scale of 1-10?
> """))
    if x == 10:
        print("Attaboy! Stay positive!\n")
    elif x >= 8:
        print("Sounds lovely! Keep on truckin'!\n")
    elif x >= 6:
        print("Chin up, buttercup!\n")                    
    elif x >= 4:            
        print("I recommend some hot chocolate and a hug, maybe...\n")               
    elif x >= 2:
        print("Dude, are you ok?\n")                   
    else:
        print("Geez!!! You might as well just go back to bed!\n")
good_day()

# Part 2
x = input("Enter your first adjective: ")
y = input("Enter your second adjective: ")

def python_props(x, y):
    print(f"Python is {x} and {y}!\n")
python_props(x, y)

# Part 3
rstring = input("""Enter the string that you'd like randomized!
> """)
def rand(x):
    from random import choice
    print(''.join(choice((str.upper, str.lower))(c) for c in rstring))
rand(rstring)