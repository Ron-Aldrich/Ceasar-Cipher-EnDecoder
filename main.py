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


while(True):
    print("=== Caesar Cipher 13 ===")
    print("1. Encode")
    print("2. Decode")

    choice = input("Choose an option: ")
    text = input("Enter your text: ")

    if choice == "1":
        print("Encoded text:", encode(text))
    elif choice == "2":
        print("Decoded text:", decode(text))
    else:
        print("Please Try Again!")
        break
        



