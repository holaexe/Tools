import os
import time

def ip_pinger():
    param = "-n 1" if os.name == "nt" else "-c 1"
    ip = input("Enter Target IP >> ")
    times = int(input(f"How many times? >> "))
    try:
        for i in range(times):
            os.system(f"ping {param} {ip}")
            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == '__main__':
    ip_pinger()