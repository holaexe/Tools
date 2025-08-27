import requests
import os
import time

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def info():
    code = input("Enter Invite Code >> ")
    output_option = input("Would you like to put all results into a output.txt [Y or N] >> ")
    try:
        output = None
        r = requests.get(f"https://discord.com/api/v10/invites/{code}?with_counts=True")
        data = r.json()
        guild = data.get("guild", {})
        if r.status_code == 200:
            print("-" * 25 + "Server Info" + "-" * 25)
            for key, value in guild.items():
                output_lines = f"{key} :3> {value}"
            output_lines.append(output)
        else:
            print("Server Not Found")
    except Exception as e:
        print(f"Error >> {e}")

if __name__ == '__main__':
    info()
