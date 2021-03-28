from sys import argv, exit


def main():
    if len(argv) == 2:  # Chec arguments of command line
        ban_list = []
        with open(argv[1]) as f:  # Open file "banned.txt" and convert in to list (word by word)
            for word in f.read().split():
                ban_list.append(word)

        message = input("What message would you like to censor?\n").split()
        censor_list = []

        for word in message:  # Check each word for a match in the dictionary
            if word.lower() in ban_list:  # If word in dictionary: Replace each letter with "*"
                censor_list.append("*" * len(word))
            else:
                censor_list.append(word)
        print(" ".join(censor_list))
    else:
        print("Usage: python bleep.py dictionary")
        exit(1)


if __name__ == "__main__":
    main()
