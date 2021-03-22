from cs50 import get_float
from math import floor


def main():
    while True:
        d = get_float("Change owed: ")  # Asking the user for a number(dollars_owed)
        c = floor(d * 100)  # cents_owed

        if c > 0:
            break

    q = c // 25  # quarters
    d = (c % 25) // 10  # dimes
    n = ((c % 25) % 10) // 5  # nickels
    p = ((c % 25) % 10) % 5  # pennies

    print(q + d + n + p)


if __name__ == "__main__":
    main()
