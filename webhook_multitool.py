import time
import os
from colorama import Fore
import requests
import sys
webhook = None

def ascii_art():
    ascii = Fore.GREEN + f"""
:::       ::: :::::::::: :::::::::  :::    :::  ::::::::   ::::::::  :::    :::       ::::::::  :::    ::: ::::::::::: 
:+:       :+: :+:        :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:   :+:       :+:    :+: :+:    :+:     :+:     
+:+       +:+ +:+        +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+  +:+        +:+        +:+    +:+     +:+     
+#+  +:+  +#+ +#++:++#   +#++:++#+  +#++:++#++ +#+    +:+ +#+    +:+ +#++:++         +#++:++#++ +#++:++#++     +#+     
+#+ +#+#+ +#+ +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+  +#+               +#+ +#+    +#+     +#+     
 #+#+# #+#+#  #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#   #+#       #+#    #+# #+#    #+#     #+#     
  ###   ###   ########## #########  ###    ###  ########   ########  ###    ###       ########  ###    ### ########### 
"""
    print(ascii)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def store_webhook():
    global webhook
    webhook = input("Enter Webhook >> ")
    try:
        s = requests.get(webhook)
        if s.status_code == 200:
            print("-Webhook Valid-")
            for i in range(100):
                print(f"\rStoring Webhook {i+1}%", flush=True, end="")
                sys.stdout.flush()
                time.sleep(0.01)
            print()
        elif s.status_code in [400, 404, 403, 402, 401]:
            print(f"-Webhook Invalid - Status Code > {s.status_code}-")
        else:
            print(f" Status Code > {s.status_code}")

    except Exception as e:
        print("Error >> " + str(e))
        
    input("Press Enter to Return...")    
    webhook_main()

def webhook_spammer():
    global webhook
    if not webhook:
        print("No Webhook Detected <> Use Option 1 to add webhook")
        input("\nPress Enter to Return...")
        webhook_main()
    clear()
    message = input("Enter Message to Spam >> ")
    spam = int(input("How Many times do you want to spam >> "))
    payload = {
        "content": message
    }
    try:
        for i in range(spam):
            r = requests.post(webhook, json=payload)
            print(f"\rSpamming {i+1}/{spam} - Status Code > {r.status_code}", flush=True, end="")
            sys.stdout.flush()
            time.sleep(0.2)
        print()
        if r.status_code == 429:
            for i in range(10):
                print(f"\rRatelimited, Waiting {10 - i} seconds")
                sys.stdout.flush()
                time.sleep(1)
        print()
    except Exception as e:
        print("Error >> " + str(e))
    
    input("Press Enter to Return...")    
    webhook_main()

def whf():
    global webhook
    if not webhook:
        print("No Webhook Detected <> Use Option 1 to add webhook")
        input("\nPress Enter to Return...")
        webhook_main()
    clear()
    for i in range(5):
        print(f"\rStarting FXCKED in {5 - i} seconds", flush=True, end="")
        sys.stdout.flush()
        time.sleep(1)
    print()
    clear()

    names = [
        "FXCKED",
        "TRASHED",
        "DUMPED",
        "SHIT ON",
        "PISSED ON"
    ]

    messages = [
        "#  FXCKED @everyone",
        "#  WEBHOOK TRASHED @everyone",
        "#  EZ WEBHOOK MASS @everyone"
    ]
    for idx in range(100):
        nm = names[idx % len(names)]
        msg = messages[idx % len(messages)]
        payload = {
            "username": nm,
            "content": msg
        }
        r = requests.post(webhook, json=payload)
        if r.status_code == 404:
            print("Invalid Webhook URL")
            webhook = None
            print("\nEnter New webhook Via Option 1")
        if r.status_code == 429:
            retry_after = r.json().get("retry_after", 1)
            for sec in range(int(float(retry_after)), 0, -1):
                print(f"\rRatelimited! Waiting {sec} seconds...", end="", flush=True)
                time.sleep(1)
            continue
        
        print(f"\rSuccessful Spam {idx+1}/100 - Status Code > {r.status_code}", flush=True, end="")
        sys.stdout.flush()
        time.sleep(0.1)

    print()
    d = requests.delete(webhook)
    print(f"Successfully deleted Webhook - Status Code > {d.status_code}")
    print("\nWEBHOOK SUCCESSFULLY FXCKED (Enter new Webhook in option 1)")
    webhook = None
    input("Press Enter to Return...")
    webhook_main()

def webhook_delete():
    global webhook
    if not webhook:
        print("No Webhook Detected <> Use Option 1 to add webhook")
        input("\nPress Enter to Return...")
        webhook_main()
    delete_option = input(f"Are you sure your about to delete your webhook? [Y or N] >> ")
    delete_normal = delete_option.strip().lower()
    if delete_normal == 'y':
        r = requests.delete(webhook)
        if r.status_code in [204, 200]:
            print("Successfully Deleted webhook")
        else:
            print(f"Status Code >> {r.status_code}")
    elif delete_normal == 'n':
        webhook_main()
    
def webhook_info():
    if not webhook:
        print("No Webhook Detected <> Use Option 1 to add webhook")
        input("\nPress Enter to Return...")
        webhook_main()
    try:
        clear()
        r = requests.get(webhook)
        data = r.json()
        for key, value in data.items():
            print(f"{key} :3> {value}")
    except Exception as e:
        print(f"Error: {e}")

    input("Press Enter to Return...")
    webhook_main()

def webhook_main():
    clear()
    ascii_art()
    print(" " * 20 + "Welcome to Webhook Fucker / THIS IS ALL MADE FOR EDUCATION AND RESEARCH PURPOSES" + " " * 20)
    print("=" * 120)
    print("\n                                     [1] - Store Webhook (MUST DO FIRST)            [4] - Webhook Delete")
    print("                                     [2] - Webhook FXCKED (premade)                 [5] - Webhook Info")
    print("                                     [3] - Webhook Spammer                          [99] - Exit")
    option = input("Option >> ")
    if option == '1':
        store_webhook()
    elif option == '2':
        whf()
    elif option == '3':
        webhook_spammer()
    elif option == '4':
        webhook_delete()
    elif option == '5':
        webhook_info()             
    elif option  == '99':
        print("Peace Out")
        time.sleep(0.5)
        sys.exit()
    else:
        print("Invalid Input")
        input("\nPress Enter to return")
        clear()
        webhook_main()