#!/usr/bin/env python3
from sys import argv, exit  # import argv


def main():

    def cipher_text(message: str, k: int) -> str:  # Change each letter by increasing the key(by "Ascii" table)
        text_list = []
        for i in message:
            if i.isupper():
                text_list.append(chr((ord(i) - 65 + k) % 26 + 65))
            elif i.islower():
                text_list.append(chr((ord(i) - 97 + k) % 26 + 97))
            else:
                text_list.append(i)

        ciphertext = ''.join(text_list)
        return ciphertext


# If 2 command line arguments are entered and the second is a number, the program will run
    if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) > 0:
        key = int(argv[1])
        text = input("plaintext: ")
        print("ciphertext:", cipher_text(text, key))
    else:
        print("Usage: python caesar.py k")
        exit(1)


if __name__ == "__main__":
    main()
