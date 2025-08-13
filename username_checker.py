import requests
import os
import time
from colorama import Fore

def ascii():
    ascii = f""" {Fore.LIGHTMAGENTA_EX}

'##::::'##::'######::'########:'########::'##::: ##::::'###::::'##::::'##:'########:::::'######::'##::::'##:'########::'######::'##:::'##:'########:'########::
 ##:::: ##:'##... ##: ##.....:: ##.... ##: ###:: ##:::'## ##::: ###::'###: ##.....:::::'##... ##: ##:::: ##: ##.....::'##... ##: ##::'##:: ##.....:: ##.... ##:
 ##:::: ##: ##:::..:: ##::::::: ##:::: ##: ####: ##::'##:. ##:: ####'####: ##:::::::::: ##:::..:: ##:::: ##: ##::::::: ##:::..:: ##:'##::: ##::::::: ##:::: ##:
 ##:::: ##:. ######:: ######::: ########:: ## ## ##:'##:::. ##: ## ### ##: ######:::::: ##::::::: #########: ######::: ##::::::: #####:::: ######::: ########::
 ##:::: ##::..... ##: ##...:::: ##.. ##::: ##. ####: #########: ##. #: ##: ##...::::::: ##::::::: ##.... ##: ##...:::: ##::::::: ##. ##::: ##...:::: ##.. ##:::
 ##:::: ##:'##::: ##: ##::::::: ##::. ##:: ##:. ###: ##.... ##: ##:.:: ##: ##:::::::::: ##::: ##: ##:::: ##: ##::::::: ##::: ##: ##:. ##:: ##::::::: ##::. ##::
. #######::. ######:: ########: ##:::. ##: ##::. ##: ##:::: ##: ##:::: ##: ########::::. ######:: ##:::: ##: ########:. ######:: ##::. ##: ########: ##:::. ##:
:.......::::......:::........::..:::::..::..::::..::..:::::..::..:::::..::........::::::......:::..:::::..::........:::......:::..::::..::........::..:::::..::
                    DISCLAIMER: All results are NOT guarenteed
"""
    print(ascii)

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def username_checker():
    valid_results = []
    invalid_results = []
    username = input("\nEnter Username to Search >> ")
    output = input("Would you like to Store results into output.txt? [Y or N] >> ")
    if output.lower().strip() == 'y':
        output = True
    elif output.lower().strip() == 'n':
        output = False
    try:
        platforms = {
    "Youtube": {
        "url": f"https://youtube.com/@{username}",
        "error_msg": "404 Not Found"  # YouTube returns 404 for non-existent users
    },
    "Twitter (X)": {
        "url": f"https://twitter.com/{username}",
        "error_msg": "This account doesn’t exist",  # Check page content
        "check_type": "text"  # Look for this text in HTML
    },
    "Instagram": {
        "url": f"https://instagram.com/{username}",
        "error_msg": "Sorry, this page isn't available.",
        "check_type": "text"
    },
    "TikTok": {
        "url": f"https://tiktok.com/@{username}",
        "error_msg": "Couldn't find this account",
        "check_type": "text"
    },
    "Facebook": {
        "url": f"https://facebook.com/{username}",
        "error_msg": "This page isn't available",  # Also check for redirects
        "check_type": "text+redirect"
    },
    "Reddit": {
        "url": f"https://reddit.com/user/{username}",
        "error_msg": "Sorry, nobody on Reddit goes by that name.",
        "check_type": "text"
    },
    "GitHub": {
        "url": f"https://github.com/{username}",
        "error_msg": "404 Not Found"  # GitHub returns 404
    },
    "Twitch": {
        "url": f"https://twitch.tv/{username}",
        "error_msg": "This channel is unavailable",
        "check_type": "text"
    },
    "Pinterest": {
        "url": f"https://pinterest.com/{username}",
        "error_msg": "Sorry, we couldn't find that one",
        "check_type": "text"
    },
    "LinkedIn": {
        "url": f"https://linkedin.com/in/{username}",
        "error_msg": "This page doesn't exist",
        "check_type": "text",
        "headers": {"User-Agent": "Mozilla/5.0"}  # Avoid bot detection
    },
    "Snapchat": {
        "url": f"https://snapchat.com/add/{username}",
        "error_msg": "Sorry, we couldn't find",
        "check_type": "text"
    },
    "Discord": {
        "url": f"https://discord.com/users/{username}",  # May not work, API is better
        "error_msg": "404 Not Found",  # Discord might not expose this easily
        "check_type": "http_status"
    },
    "Medium": {
        "url": f"https://medium.com/@{username}",
        "error_msg": "404",
        "check_type": "http_status"
    },
    "Quora": {
        "url": f"https://quora.com/profile/{username}",
        "error_msg": "Page Not Found",
        "check_type": "text"
    },
    "Steam": {
        "url": f"https://steamcommunity.com/id/{username}",
        "error_msg": "The specified profile could not be found",
        "check_type": "text"
    }
}

        for name, info in platforms.items():
            url = info["url"]
            error_msg = info["error_msg"]
            r = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
            })
            if error_msg in r.text:
                result = f"{name} - {error_msg} found in {url}"
                invalid_results.append(result)
            elif r.status_code in [404, 403, 402, 401, 400]:
                result = f"{name} - Status Code >> {r.status_code} - User Not found >> {url}"
                invalid_results.append(result)
            elif r.status_code == 200:
                result = f"{name} - Status Code > {r.status_code} - User Found >> {url}"
                valid_results.append(result)
            else:
                result = f"{name} - Unknown Error >> {r.status_code}"
                invalid_results.append(result)
        print("=" * 25 + "Valid Username info" + "=" * 25)
        for item in valid_results:
            print(item)
        print("=" * 25 + "Invalid Username info" + "=" * 25)
        for item in invalid_results:
            print(item)
        if output:
            with open("output.txt", "w") as f:
                f.write("=" * 25 + "Valid Username info" + "=" * 25 + "\n")
                for item in valid_results:
                    f.write(item + "\n")
                f.write("=" * 25 + "Invalid Username info" + "=" * 25 + "\n")
                for item in invalid_results:
                    f.write(item + "\n")
    except Exception as e:
        print(f"Error >> {e}")
    input("\nPress Enter to return...")
    main()

def main():
    clear()
    ascii()
    print("                                     [1] Username check")
    option = input("Enter option >> ")
    if option == '1':
        username_checker()
    else:
        print("Returning")
        time.sleep(0.5)
        main()



if __name__ == '__main__':
    main()