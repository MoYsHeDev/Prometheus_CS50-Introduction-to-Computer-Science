# Asking the user for a number
while True:
    height = input("Height: ")
    if height.isdigit():
        h = int(height)
        if 1 <= h <= 8:
            break

n = 1
for i in range(h):  # Printing lines
    for j in range(h - n):  # Printing spaces
        print(" ", end="")
    for k in range(n):  # Printing hashes
        print("#", end="")
    n += 1
    print()
