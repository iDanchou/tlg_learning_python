def virus():
    while True:
        print("UPLOADING.")
        print("UPLOADING....")
        print("UPLOADING.........")
        print("VIRUS HAS BEEN UPLOADED\n")
        print("""Alright, now the virus has been placed into the system.
Let's get a look at that password hash so we can see about cracking it.\n""")
        enter = input("\nPress ENTER to show the hash. \n")
        if enter == "":
            print("$2$y10$6z7GKa9kpDN7kC31.fd0/toY7/x64WUDYBH")
            break
        else:
            print("\nCome on! Let's do it right this time.\n")
            continue
virus()