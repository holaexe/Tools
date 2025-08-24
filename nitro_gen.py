import requests
import os
from colorama import Fore
import time
import random
import string

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def ascii_art():
    ascii = f""" {Fore.LIGHTBLUE_EX}
ooooo      ooo  o8o      .                             .oooooo.                          
`888b.     `8'  `"'    .o8                            d8P'  `Y8b                         
 8 `88b.    8  oooo  .o888oo oooo d8b  .ooooo.       888            .ooooo.  ooo. .oo.   
 8   `88b.  8  `888    888   `888""8P d88' `88b      888           d88' `88b `888P"Y88b  
 8     `88b.8   888    888    888     888   888      888     ooooo 888ooo888  888   888  
 8       `888   888    888 .  888     888   888      `88.    .88'  888    .o  888   888  
o8o        `8  o888o   "888" d888b    `Y8bod8P'       `Y8bood8P'   `Y8bod8P' o888o o888o 
"""
    print(ascii)

webhook = None

def nitro_options():
    global webhook
    webhook_option = input("Would you like to send the generated codes in a webhook? [Y or N] >> ")
    if webhook_option.lower().strip() == 'y':
        webhook = input("Enter Webhook URL >> ")
        try:
            response = requests.get(webhook)
            if response.status_code == 200:
                print("-Webhook Valid-")
                for i in range(100):
                    print(f"\rStoring Webhook {i+1}%", flush=True, end="")
                    time.sleep(0.01)
                print()
            else:
                print(f"-Webhook Invalid - Status Code > {response.status_code}-")
        except Exception as e:
            print("Error >> " + str(e))
        input("Press Enter to Continue...")
    elif webhook_option.lower().strip() != 'n':
        print("Invalid Option")
        time.sleep(0.5)
        main()
        return

    infinite = input("Would you like it to run infinitely? [Y or N] >> ")
    if infinite.lower().strip() == 'y':
        nitro_gen(infinite=True)
    elif infinite.lower().strip() == 'n':
        nitro_gen(infinite=False)
    else:
        print("Invalid Option")
        main()

def nitro_gen(infinite=False):
    global webhook
    clear()
    ascii_art()
    print("Generating Nitro Codes...")
    try:
        if infinite:
            print("Running infinitely... Press Ctrl+C to stop.")
            while True:
                code = f"discord.gift/{''.join(random.choices(string.ascii_letters + string.digits, k=16))}"
                print(f"\rGenerated Code: {code}")
                if webhook:
                    try:
                        requests.post(webhook, json={"content": code})
                    except Exception as e:
                        print(f"Error sending to webhook: {e}")
                time.sleep(0.1)
        else:
            codes = []
            for i in range(100):
                code = f"discord.gift/{''.join(random.choices(string.ascii_letters + string.digits, k=16))}"
                codes.append(code)
                print(f"\rGenerated Code: {code}")
                time.sleep(0.1)
            print("\nCodes generated successfully!")
            if webhook:
                for code in codes:
                    try:
                        requests.post(webhook, json={"content": code})
                    except Exception as e:
                        print(f"Error sending to webhook: {e}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to Return...")
    main()

def main():
    clear()
    ascii_art()
    print("                                  [1] Run Nitro Gen")
    option = input("Enter Option >> ")
    if option.strip() == '1':
        nitro_options()
    else:
        print("Invalid Option")
        input("Press Enter to Return...")
        main()

if __name__ == "__main__":
    main()
