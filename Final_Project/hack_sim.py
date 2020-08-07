#import help_function
#import virus_function

login_att = 0  #  VALUE OF LOGIN ATTEMPTS THAT WILL INCREMENT WITH FAILED ATTEMPTS 
password = "H@CK3R" #  SETTING PASSWORD THAT USER WILL NEED TO FIND
commands = {"ip addr":"127.0.4.21"}  #  WORKING ON USING DICT FOR CERTAIN VALUES
name = input("""Welcome. What is your name?
> """)

print(f"""~~~~~~ {name.upper()} ENTERS THE H@CK3R SIMULATOR ~~~~~~ \n
This will be a test of knowledge and potential.
I'll need you to focus and keep your eyes active.
There are more breadcrumbs than you may think.\n""")

print(f"USERNAME: {name.upper()}")  # TRANS USER NAME INTO ALL UPPERCASE
 
while True:  # CREATES A WHILE LOOP THAT FORCES USER TO GUESS CORRECT PASSWORD
    if input("PASSWORD: ") == password:
        print("\n")
        print(f"Successfully logged in after {login_att} attempts\n")
        print("""00100010101100010010011
01001011110001001001001
01101110100100010010010\n
Great eyes, You've made it into the test account. 
Let's check the wireless networks and see who needs to revamp their security.
If you're not a linux user feel free to use the help command.\n""")
        break
    else:
        print("\n Remember that thing I said about breadcrumbs? Take another look.\n")
        login_att += 1  # FOR EVERY INCORRECT GUESS USER WILL BE REROUTED TO INPUT AGAIN
        continue

while True:
    if input() == "help":
        helping()
    elif input() == ""
#  help_function.helping() IMPORTED HELP FUNCTION BEING CALLED
#  virus_function.virus() IMPORTED VIRUS FUNCTION 