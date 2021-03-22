# Asking the user for a number
while True:
    h = input("Height: ")
    if h.isdigit() and 1 <= int(h) <= 8:
        break

height = int(h)
hashes = 1


for i in range(height):  # Printing lines
    spaces = height - hashes
    print(" " * spaces, end="")
    print("#" * hashes, end="")
    print("  ", end="")
    print("#" * hashes, end="")
    print()
    hashes += 1
