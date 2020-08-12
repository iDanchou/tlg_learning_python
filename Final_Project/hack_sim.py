import time
import sys
import ipaddress
from datetime import date
import random
import pyfiglet

print("\n")

from progress_bar import probar

print("\n")

def nmap():
    print(f"""\n    {name.lower()}@training-wheels:~$ sudo nmap -sn 192.168.0.1/24
    Starting Nmap 5.21 ( http://nmap.org ) at {date.today()}
    Nmap scan report for FOSS 192.168.1.1
    Host is down.
    MAC Address: E0:A1:D5:72:5A:5C (Unknown)
    Nmap scan report for WINE 192.168.1.91
    Host is down.
    Nmap scan report for TUX 192.168.0.6
    Host is up (0.12s latency).\n""")

def ifconfig():
    print(f"""\n    {name.lower()}@training-wheels:~$ ifconfig
    wlan0 Link encap:Ethernet HWaddr 70:f1:a1:c2:f2:e9
    inet addr:192.168.0.1 Mask:255.255.255.0
    inet6 addr: fe80::73f1:a1ef:fec2:f2e8/64 Scope:Link
    UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1\n""")

def helping():
    print("""\nWe all need a little help sometimes. Here are some commands that can help move you along.\n
    *'ls -a' to get a look at the files within the system, the '-a' includes hidden files as well.
    *'touch' to create a file.
    *'iwlist scan' to see currently available wireless access points.
    *'iwconfig' to configure wireless internet connection.
    *'ifconfig' to find IP address range on the current network.
    *'nmap' is a tool to scan networks.\n""")

def iwlist():
    print("""\n    SSID: It_Burns_When_IP  CHAN: 6  SEC: SECURED  RATE: 62 Mbit/s  FIREWALL: ENABLED
    SSID: BILL_CLINTERNET  CHAN: 1  SEC: UNSECURED  RATE: 54 Mbit/s  FIREWALL: DISABLED
    SSID: Silence_of_the_LANS  CHAN: 11  SEC: SECURED  RATE 68 Mbit/s  FIREWALL: ENABLED
    SSID: WINternet_is_Coming  CHAN: 4  SEC: SECURED  RATE 46 Mbit/s  FIREWALL: DISABLED\n""")

def iwconfig():
    print("""\n    Please enter the SSID and password of the wireless network you wish to join.
    If the network is unsecured, press ENTER after inputting the SSID.\n""")
    while True:
        wifi = input("")
        if wifi.upper() == "BILL_CLINTERNET":
            time.sleep(3)
            print("\nConnection Successful\n")
            break
        elif wifi.upper() == ssid[0] or ssid[1] or ssid[2]:
            print("\nLook for an unsecured access point, you haven't learned to crack networks yet.\n")
            continue
        else:
            print("\nThis doesn't look like one of the options on the list, run that command again.\n")
            continue

login_att = 1  #  VALUE OF LOGIN ATTEMPTS THAT WILL INCREMENT WITH FAILED ATTEMPTS 
ascii_banner = pyfiglet.figlet_format("GRADUATION!")
ssid = ["It_Burns_When_IP".upper(), "Silence_of_the_LANS".upper(), "WINternet_is_Coming".upper()]
personal_ip = '192.168.0.1'
password = "H@CK3R" #  SETTING PASSWORD THAT USER WILL NEED TO FIND
name = input("""To keep communications up and our heads down, you'll need a call sign. Choose something classy and enter it below. 
$ """)

print("\n")

while True:  # NAME LOOP
    ans = input(f"""    So you decided on '{name.lower()}'? Last chance to change your mind before we lock it in.
    Press ENTER to continue or press 'q' to choose another sign. 
    $ """)
    if ans == "":
        print("\n")
        break
    elif ans == "q":
        name = input("""\nTo keep communications up and our heads down, you'll need a call sign. Choose something classy and enter it below. 
    $ """)
        print("\n")
        break
    else:
        print("\nThink hard about this one, once the mission begins you'll be seeing the name you chose.\n")
        continue

from loading_bar import load  # LOADING BAR

print("\n")

print(f"""~~~~~~ {name.upper()} ENTERS THE H@CK3R SIMULATOR ~~~~~~ \n
This is a test of attention to detail and potential.
I'll need you to focus and keep your eyes active.
There are more breadcrumbs than you may think.\n""")

print(f"USERNAME: {name.upper()}")  # TRANSFORM USER NAME INTO ALL UPPERCASE
 
while True:  # PASSWORD LOOP
    if input("PASSWORD: ") == password:
        time.sleep(2)
        print("\n")
        print(f"Successfully logged in after {login_att} attempts\n")
        print("""    Great eyes, You've made it into the throwaway account. You might have some potential here. 
    Let's check the wireless networks and see who needs to revamp their security.
    If you're not a linux user feel free to use the help command.\n""")
        break
    else:
        print("\nRemember that thing I said about breadcrumbs? Take another look.\n")
        login_att += 1  # FOR EVERY INCORRECT GUESS USER WILL BE REROUTED TO INPUT AGAIN
        continue

while True:  # IWLIST SCAN LOOP
    answer = input("")
    if answer.lower() == "help":  # if user types help, the help function will run
        print("\n")
        helping()
        continue
    elif answer.lower() == "iwlist scan":
        iwlist()
        break
    else:
        print("\nIf you're stuck, type in that help command so we can keep moving.\n")
        continue

while True:  # IWCONFIG LOOP
    iw = input("")
    if iw.lower() == "help":
        helping()
    elif iw.lower() == "iwconfig":
        iwconfig()
        break
    else:
        print("\nBefore we can go any further we need to get into that network!\n")
        continue

print("\nNow that we're connected, let's use a terminal command to figure out the IP address range for us.\n")

while True:  # IFCONFIG LOOP
    ifc = input("")
    if ifc.lower() == "help":
        helping()
    elif ifc.lower() == "ifconfig":
        ifconfig()
        break
    else:
        print("\nOnce we get the address range and subnet mask we can really get the wheels turning. Try it again.\n")
        continue

while True:  # NMAP LOOP
    ip_addr = input("""Enter that IP address from the last command and let's see which devices are joined to the network.
    > """)
    if ip_addr.lower() == "help":
        helping()
    elif ip_addr == personal_ip:
        nmap()
        break
    else:
        print("\nThis is either where stars are born, or you throw in the towel. Which will it be kid?\n")
        continue

print("""\nWe don't have the private ssh key for the machine,
so we're going to crack this password the old fashioned way. Brute force.\n""")

print("When you ran that last command, someone special to Linux appeared.\n")

while True:
    let_to_num = input("""\nIf you were able to find it, type that into the terminal.
# """)
    if let_to_num.lower() == "help":
        helping()
    elif let_to_num.lower() == "tux":
        print("""\nWe're going to take this phrase and run it through a cipher
to see if the password might be an alphanumerical translation.""")
        numbers = [ord(let_to_num) - 96 for let_to_num in let_to_num] # CIPHERS LETTERS INTO NUMBERS
        print("\n")
        print(numbers)  # PRINTS THE FINAL RESULT
        break
    elif let_to_num.lower() == "nmap":  # WILL RERUN THE NMAP FUNCTION FOR THE HINT
        nmap()
    else:
        print("\nLook for one thing that stands apart from the rest.\n")
        continue

brute = str(input("\nEnter the number you received from the cipher: "))

guess = " "
count = 0
while guess != brute:
    guess = str(random.randint(100000,999999))
    count += 1

    print("=> " + guess)

    if guess == brute:
        print("\nThe password was cracked after " + count + " guesses!")
        print("""\nYou made it the whole way and cracked the code.
Now that you have the password, type it in after the IP address and enjoy your victory.\n""")
        break

while True:
    final = input(f"{name.lower()}@training-wheels:~$ ssh tux@")
    last_pass = input(f"{name.lower()}@training-wheels:~$ tux@192.168.0.6 ")
    if final == '192.168.0.1' and last_pass == "202124":
        print(ascii_banner)
        sys.exit()
    else:
        print("This is the home stretch! Finish strong!")
        continue