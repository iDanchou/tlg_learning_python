import time
import sys

def helping():
    print("""\nWe all need a little help sometimes. Here are some commands that can help move you along.\n
    *'ls' to get a look at the files within the system.
    *'ping' to gather the IP address of the machine.
    *'touch' to create a file.
    *'w' to see who is currently logged in and what they're doing.
    *'iwlist scan' to see currently available wireless access points.
    *'iwconfig' to configure wireless internet connection.\n""")

def decrypter():
    while True:
        print("DECRYPTION TOOL HAS BEEN UPLOADED\n")
        print("""Alright, now the cracker has been integrated with the system.
        Let's get a look at that password hash so we can see about cracking it.\n""")
        enter = input("\nPress ENTER to show the hash. \n")
        if enter == "":
            print("$2$y10$6z7GKa9kpDN7kC31.fd0/toY7/x64WUDYBH")
            break
        else:
            print("\nRelax and take the pressure off. It's one key. Let's do it right this time.\n")
            continue

def iwlist():
    print("""\n    SSID: It_Burns_When_IP  CHAN: 6  SEC: SECURED  RATE: 62 Mbit/s
    SSID: BILL_CLINTERNET  CHAN: 1  SEC: UNSECURED  RATE: 54 Mbit/s
    SSID: Silence_Of_The_LANS  CHAN: 11  SEC: SECURED  RATE 68 Mbit/s
    SSID: WINternet_Is_Coming  CHAN: 4  SEC: SECURED  RATE 46 Mbit/s\n
    """)

def iwconfig():
    print("""\n    Please enter the SSID and password of the wireless network you wish to join.
    If the network is unsecured, press ENTER after inputting the SSID.\n""")
    while True:
        wifi = input("")
        if wifi.upper() == "BILL_CLINTERNET":
            time.sleep(3)
            print("\n You have connected to BILL_CLINTERNET\n")
            break
        else:
            print("Look for an unsecured access point, you haven't learned to crack networks yet.\n")
            continue

login_att = 0  #  VALUE OF LOGIN ATTEMPTS THAT WILL INCREMENT WITH FAILED ATTEMPTS 
password = "H@CK3R" #  SETTING PASSWORD THAT USER WILL NEED TO FIND
command = {"ip addr":"127.0.4.21"}  #  WORKING ON USING DICT FOR CERTAIN VALUES
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
        time.sleep(2)
        print(f"Successfully logged in after {login_att} attempts\n")
        print("""Great eyes, You've made it into the throwaway account. You might have some potential here. 
Let's check the wireless networks and see who needs to revamp their security.
If you're not a linux user feel free to use the help command.\n""")
        break
    else:
        print("\n Remember that thing I said about breadcrumbs? Take another look.\n")
        login_att += 1  # FOR EVERY INCORRECT GUESS USER WILL BE REROUTED TO INPUT AGAIN
        continue

while True:
    answer = input("")
    if answer.lower() == "help":  # if user types help, the help function will run
        helping()
        continue
    elif answer.lower() == "iwlist scan":
        iwlist()
        print("")
        break
    else:
        print("If you're stuck, type in that help command so we can keep moving.")
        continue

while True:
    iw = input("")
    if iw.lower() == "help":
        helping()
    elif iw.lower() == "iwconfig":
        iwconfig()
        break
    else:
        print("Before we can go any further we need to get into that network!")
        continue

print("Now that we're connected, let's use the nmap command to get some IP addresses on the network.")