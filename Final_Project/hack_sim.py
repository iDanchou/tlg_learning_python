import time
import sys
import ipaddress
from datetime import date

print("\n")

from progress_bar import probar

print("\n")

def nmap():
    print(f"""\n    {name.lower()}@training-wheels:~$ sudo nmap -sn 192.168.0.1/24
    Starting Nmap 5.21 ( http://nmap.org ) at {date.today()}

    Nmap scan report for 192.168.1.1
    Host is down.\n
    MAC Address: E0:A1:D5:72:5A:5C (Unknown)
    Nmap scan report for 192.168.1.91
    Host is down.\n
    Nmap scan report for 192.168.0.6
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

print("""There's a tool known as SSH(Secure Shell) that will allow remote access,
we'll be able to control that machine as if it was sitting directly in front of us.""")

print("""However, seeing as we don't currently have access to the private ssh key for the machine,
we're going to crack this password the old fashioned way.""")