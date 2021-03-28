#!/usr/bin/env python3
from sys import argv, exit


def main():
    """ Create function "cipher_text"
    Each letter of the incoming message must be encrypted using the Vigenere method.
    Only upper and lower case letters should be encrypted, punctuation marks and numbers remain unencrypted.
    """
    def cipher_text(message: str, k: str) -> str:
        k_list, mes_list = [], []

        for i in k:  # Convert a "key" string to a list, using the Vigenère method (A = 0, Z = 25)
            k_list.append(ord(i.upper()) % 65)

        j = 0  # Index k_list
        for i in range(len(message)):
            if message[i].isupper():
                mes_list.append(chr((ord(message[i]) - 65 + k_list[j]) % 26 + 65))
                j = (j + 1) % len(k_list)
            elif message[i].islower():
                mes_list.append(chr((ord(message[i]) - 97 + k_list[j]) % 26 + 97))
                j = (j + 1) % len(k_list)
            else:
                mes_list.append(message[i])

        return ''.join(mes_list)  # Return a list of encrypted characters, converting it to a string

    if len(argv) == 2 and argv[1].isalpha():
        key = argv[1]
        text = input("plaintext: ")
        print("ciphertext:", cipher_text(text, key))
    else:
        print("Usage: python vigenere.py k")
        exit(1)


if __name__ == "__main__":
    main()
