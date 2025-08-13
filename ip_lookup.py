import requests
import os
import time
from colorama import Fore

def clear():
    if os.name  == 'nt': 
        os.system("cls")
    else:
        os.system("clear")

def ascii():
    ascii = f""" {Fore.BLUE}
    

 @@@ @@@@@@@           @@@       @@@@@@   @@@@@@  @@@  @@@ @@@  @@@ @@@@@@@ 
 @@! @@!  @@@          @@!      @@!  @@@ @@!  @@@ @@!  !@@ @@!  @@@ @@!  @@@
 !!@ @!@@!@!           @!!      @!@  !@! @!@  !@! @!@@!@!  @!@  !@! @!@@!@! 
 !!: !!:               !!:      !!:  !!! !!:  !!! !!: :!!  !!:  !!! !!:     
 :    :       .......  : ::.: :  : :. :   : :. :   :   :::  :.:: :   :      
              : :: : :                                                      """
    print(ascii)

def ip_lookup():
    ip = input("\n\nEnter Target IP >> ")
    output_option = input("Do you want to store results into a output.txt? [Y or N] >> ")
    output_normal = output_option.strip().lower()
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            print(f"-" * 20 + "IP INFO" + "-" * 20)
            for key, value in data.items():
                print(f"{key} :3> {value}")
            print("-" * 20 + "RAW DATA" + "-" * 20)
        else:
            print(f"Script Malfunctioned or IP invalid, Status Code >> {response.status_codes}")

    except Exception as e:
        print(e)

    if output_normal == 'y':
        with open("output.txt", "w") as o:
            o.write("-" * 20 + "IP INFO" + "-" * 20 + "\n")
            for key, value in data.items():
                o.write(f"{key} :3> {value} " + "\n")
            o.write("-" * 20 + "RAW INFO" + "-" * 20 + "\n")
            o.write(str(data) + "\n")
    return data

def main():
    clear()
    ascii()
    print("                     [1] IP Lookup")
    option = input("Option >> ")
    if option == '1':
        ip_lookup()
    else:
        print("Returning...")
        time.sleep(0.5)
        main()

input("Press Enter to return")
main()
final = ip_lookup()
if __name__ == '__main__':
    print(final)
