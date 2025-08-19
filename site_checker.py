import requests
from colorama import Fore
import os
import time

def ascii():
    ascii = f"""  {Fore.CYAN}

 #     #                                                                                         
 #  #  # ###### #####   ####  # ##### ######     ####  #    # ######  ####  #    # ###### #####  
 #  #  # #      #    # #      #   #   #         #    # #    # #      #    # #   #  #      #    # 
 #  #  # #####  #####   ####  #   #   #####     #      ###### #####  #      ####   #####  #    # 
 #  #  # #      #    #      # #   #   #         #      #    # #      #      #  #   #      #####  
 #  #  # #      #    # #    # #   #   #         #    # #    # #      #    # #   #  #      #   #  
  ## ##  ###### #####   ####  #   #   ######     ####  #    # ######  ####  #    # ###### #    # 
                                                                                                 
"""
    print(ascii)

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def online_checker():
    site = input("Enter Website to check [https at start] >> ")
    try:
        clear()
        response = requests.get(site)
        if response.status_code == 200:
            print(f"\nSite Online >> Status Code - {response.status_code}")
        else:
            print(f"Status not 200... {response.status_code}")
    except Exception as e:
        print(f"Error >> {e}")
    input("Press Enter to return...")
    main()

def response_checker():
    site = input("Enter Website to check [https at start] >> ")
    try:
        start = time.time()
        requests.get(site)
        end = time.time()
        elapsed = end - start
        print(f"Response time >> {elapsed:.3f}")
    except Exception as e:
        print(f"Error >> {e}")
    input("Press Enter to return...")
    main()
    
def redirect_checker():
    site = input("Enter Website to check [https at start] >> ")
    try:
        r = requests.get(site, allow_redirects=True)
        print("Redirect Chain -----------------")
        for resp in r.history:
            print(f"{resp.status_code} > {resp.url}")
        print(f"Original Link >> {r.status_code} >> {r.url}")
    except Exception as e:
        print(f"Error >> {e}")
    input("Press Enter to return...")
    main()

def main():
    clear()
    ascii()
    print("                             [1] - Site Online Checker")
    print("                             [2] - Check Website Response Time")
    print("                             [3] - Check Site Redirects")
    option = input("Option >> ")
    if option == '1':
        online_checker()
    elif option == '2':
        response_checker()
    elif option == '3':
        redirect_checker()
    else:
        print("Invalid...")
        time.sleep(0.5)
        main()

if __name__ == '__main__':
    main()
