def encode(text):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + 13) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def decode(text):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - 13) % 26 + base)
            result += new_char
        else:
            result += char

    return result

def Information():
    print("""
Caesar Cipher 13 (DK13) Encoder & Decoder

Caesar Cipher 13 (DK13) is a Python-based text encryption and decryption tool that shifts each letter 13 positions forward or backward in the alphabet. It allows users to encode readable text into a simple encrypted format and decode it back to its original form. The program preserves spaces, numbers, and special characters.

Developer: Cryptors""")


while(True):
    print("=== Caesar Cipher 13 ===")
    print("1. Encode")
    print("2. Decode")
    print("4. Info")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "4":
        print("Thank you for using this tool!")
        break
    text = input("Enter your text: ")

    if choice == "1":
        print("Encoded text:", encode(text))
    elif choice == "2":
        print("Decoded text:", decode(text))
    
    else:
        print("Please Try Again!")
        break
        



