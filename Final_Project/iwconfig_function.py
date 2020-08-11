def iwlist_config():
    print("""Please enter the SSID and password of the wireless network you wish to join.
    If there is no password, press ENTER after inputting the SSID.""")
    while True:
        if input() == "BILL_CLINTERNET":
            time.sleep(3)
            print("\n You have connected to BILL_CLINTERNET")
            break
        else:
            print("Look for an unsecured access point, you haven't learned to crack networks yet.")
            continue
iwlist_config()