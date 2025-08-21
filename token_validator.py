from optparse import Option
import requests
import os
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
         os.system("clear")

def tokens_ascii():
    ascii = f""" {Fore.YELLOW}
    
 _______    _                    _     _       _  _     _                        
(_______)  | |                  (_)   (_)     | |(_)   | |        _              
    _  ___ | |  _ _____ ____     _     _ _____| | _  __| |_____ _| |_ ___   ____ 
   | |/ _ \| |_/ ) ___ |  _ \   | |   | (____ | || |/ _  (____ (_   _) _ \ / ___)
   | | |_| |  _ (| ____| | | |   \ \ / // ___ | || ( (_| / ___ | | || |_| | |    
   |_|\___/|_| \_)_____)_| |_|    \___/ \_____|\_)_|\____\_____|  \__)___/|_|    
                                                                                     
"""
    print(ascii)

def token_validator():
    clear()
    tokens_ascii()
    Option = input("Would you like to Validate Tokens from tokens.txt - [Y or N] >> ")
    if Option.strip().lower() == 'y':
        try:             
            with open("tokens.txt", "r") as f:
                tokens = [line.strip() for line in f if line.strip()]
                for token in tokens:
                    validate_tokens(token)
        except FileNotFoundError as e:
            print(f"Error >> {e}")
    elif Option.strip().lower() == 'n':
        token = input("Enter Token >> ")
        validate_tokens(token)

def validate_tokens(token):
    try:
        headers = {"Authorization": token}
        r = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if r.status_code == 200:
            print(f"Token is Valid :3 - Status code >> {r.status_code}")
        else:
            print(f"Invalid token :3 - Status code >> {r.status_code}")
    except Exception as e:
        print(f"Error >> {e}")
    input("Press Enter to Return...")
    token_validator()

if __name__ == "__main__":
    token_validator()