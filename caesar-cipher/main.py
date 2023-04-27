# a caesar cipher encoder and decoder
# TODO: input validation
from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, mode="encode"):
    msg = []
    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            if mode == "decode":
                index -= shift
            else:
                index += shift

            if index > len(alphabet)-1:
                msg.append(alphabet[index - 26])
            else:
                msg.append(alphabet[index])
            index += 1
        else:
            msg.append(char)  # non-alphabetic character
    return "".join(msg)

def app():
    print("[caesar@cipher] $ cciph")
    print(logo)
    flag = True
    while flag:  # careful, no validation for inputs
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n[caesar@cipher] $ ")
        plaintext = input("Type your message:\n[caesar@cipher] $ ").lower()
        shift = int(input("Type the shift number:\n[caesar@cipher] $ "))
        if shift > 26:
            shift = shift % 26
        msg = caesar(plaintext, shift, direction)
        print(f"\nThe {direction}d text is '{msg}'")
        
        should_repeat = input("\nRun again? [y/n]:\n[caesar@cipher] $ ")
        if should_repeat.startswith('n'):
            flag = False
        print()
    print("Exiting...")


app()
