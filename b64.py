import base64
import os
import time
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ascii():
    ascii = f""" {Fore.YELLOW}
                                                                                                                                                                                                                
BBBBBBBBBBBBBBBBB           66666666         444444444                                                    
B::::::::::::::::B         6::::::6         4::::::::4                                                    
B::::::BBBBBB:::::B       6::::::6         4:::::::::4                                                    
BB:::::B     B:::::B     6::::::6         4::::44::::4                                                    
  B::::B     B:::::B    6::::::6         4::::4 4::::4          ppppp   pppppppppyyyyyyy           yyyyyyy
  B::::B     B:::::B   6::::::6         4::::4  4::::4          p::::ppp:::::::::py:::::y         y:::::y 
  B::::BBBBBB:::::B   6::::::6         4::::4   4::::4          p:::::::::::::::::py:::::y       y:::::y  
  B:::::::::::::BB   6::::::::66666   4::::444444::::444        pp::::::ppppp::::::py:::::y     y:::::y   
  B::::BBBBBB:::::B 6::::::::::::::66 4::::::::::::::::4         p:::::p     p:::::p y:::::y   y:::::y    
  B::::B     B:::::B6::::::66666:::::64444444444:::::444         p:::::p     p:::::p  y:::::y y:::::y     
  B::::B     B:::::B6:::::6     6:::::6         4::::4           p:::::p     p:::::p   y:::::y:::::y      
  B::::B     B:::::B6:::::6     6:::::6         4::::4           p:::::p    p::::::p    y:::::::::y       
BB:::::BBBBBB::::::B6::::::66666::::::6         4::::4           p:::::ppppp:::::::p     y:::::::y        
B:::::::::::::::::B  66:::::::::::::66        44::::::44 ......  p::::::::::::::::p       y:::::y         
B::::::::::::::::B     66:::::::::66          4::::::::4 .::::.  p::::::::::::::pp       y:::::y          
BBBBBBBBBBBBBBBBB        666666666            4444444444 ......  p::::::pppppppp        y:::::y           
                                                                 p:::::p               y:::::y            
                                                                 p:::::p              y:::::y             
                                                                p:::::::p            y:::::y              
                                                                p:::::::p           y:::::y               
                                                                p:::::::p          yyyyyyy                
                                                                ppppppppp                                 
                                                                                                          
"""
    print(ascii)

def text_encode():
    text = input("Enter Text >> ")
    try:
        b64_encoded = base64.b64encode(text.encode()).decode()
        print(f"Encoded Text >> {b64_encoded}")
    except Exception as e:
        print(f"Error >> {e}")
    input("Press Enter to continue...")
    main()

def text_decode():
    text = input("Enter b64 text to Decode >> ")
    try:
        decoded = base64.b64decode(text.encode()).decode()
        print(f"Decoded Text >> {decoded}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    main()

def encode_txt_file():
    file = input("Drag and Drop txt file >> ").strip('"')
    try:
        with open(file, "r") as f:
            info = f.read()
        encoded = base64.b64encode(info.encode()).decode()
        with open(file, "w") as fw:
            fw.write(encoded)
        print(f"File Successfully Encoded >> {file}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    main()

def decode_txt_file():
    file = input("Drag and Drop File here >> ").strip('"')
    try:
        with open(file, "r") as f:
            info = f.read()
        decoded = base64.b64decode(info.encode()).decode()
        with open(file, "w") as fw:
            fw.write(decoded)
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    main()
        
def encode_py():
    file = input("Drag And drop PY File here >> ").strip('"')
    try:
        with open(file, "r") as f:
            info = f.read()
        encoded = base64.b64encode(info.encode()).decode()
        stub = f'''
import base64
exec(base64.b64decode("{encoded}").decode())
''' 
        with open(file, "w") as f:
            f.write(stub)
        print(f"Encoded >> {file}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    main()


def main():
    clear()
    ascii()
    print("\n                                       [1] - Encode Text")
    print("                                       [2] - Decode Text")
    print("                                       [3] - Encode TXT File")
    print("                                       [4] - Decode TXT file")
    print("                                       [5] - Encode PY File")
    print("                                       [6] - Decode PY File")
    option = input("user#root:3> ")
    if option == '1':
        text_encode()
    elif option == '2':
        text_decode()
    elif option == '3':
        encode_txt_file()
    elif option == '4':
        decode_txt_file()
    elif option == '5':
        encode_py()
        
        
if __name__ == '__main__':
    main()
