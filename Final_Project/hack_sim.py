login_att = 0
password = "H@CK3R"
commands = ["ip addr": "127.0.4.21"]
name = input("""Welcome. What is your name?
>  """)

print(f"""~~~~~~ {name.upper()} ENTERS THE H@CK3R SIMULATOR ~~~~~~ \n
This will be a test of knowledge and potential.
I'll need you to focus and keep your eyes active.
There are more breadcrumbs than you may think.\n""")

print(f"USERNAME: {name.upper()}")
 
while True:
    if input("PASSWORD: ") == password:
        print("\n")
        print(f"Successfully logged in after {login_att} attempts")
        print("""00100010101100010010011
01001011110001001001001
01101110100100010010010
Great eyes, You're in. Now lets see about gathering some info.\n""")
        break
    else:
        print("\n Remember that thing I said about breadcrumbs? Take another look.\n")
        login_att += 1
        continue

        