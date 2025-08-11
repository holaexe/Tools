import base64
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def text_encode():
    text = input("Enter Text >> ")
    try:
        b64_encoded = base64.b64encode(text.encode()).decode()
        print(f"Encoded Text >> {b64_encoded}")
    except Exception as e:
        print(f"Error >> {e}")
    input("Press Enter to continue...")
    clear()
    main()

def text_decode():
    text = input("Enter b64 text to Decode >> ")
    try:
        decoded = base64.b64decode(text.encode()).decode()
        print(f"Decoded Text >> {decoded}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    clear()
    main()

def encode_txt_file():
    file = input("Drag and Drop txt file >> ").strip('"')
    try:
        with open(file, "r") as f:
            info = f.read()
        encoded = base64.b64encode(info.encode()).decode()
        with open(file, "w") as file:
            file.write(encoded)
        print(f"File Successfully Encoded >> {file}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    clear()
    main()

def decode_txt_file():
    file = input("Drag and Drop File here >> ").strip('"')
    try:
        with open(file, "r") as f:
            info = f.read()
        decoded = base64.b64decode(info.encode()).decode()
        with open(file, "w") as file:
            f.write(decoded)
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")
    clear()
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
    clear()
    main()


def main():
    print("[1] - Encode Text")
    print("[2] - Decode Text")
    print("[3] - Encode TXT File")
    print("[4] - Decode TXT file")
    print("[5] - Encode PY File")
    print("[6] - Decode PY File")
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