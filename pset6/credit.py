#!/usr/bin/env python3


# check the card number for validation
def lunn_alg(number):
    # Get 2 lists (Paired and non-paired items from the end of the "card" string)
    nums = list(number)
    nums.reverse()
    pair = []
    unpair = []

    for i in range(len(nums)):
        if i % 2 == 0:
            unpair.append(int(nums[i]))
        else:
            pair.append(int(nums[i]) * 2)

    # Iterate all two-digit numbers in the list of paired elements and rewrite this number by the sum of their ranks
    for i in range(len(pair)):
        if pair[i] > 9:
            pair[i] = pair[i] // 10 + pair[i] % 10

    if sum(pair + unpair) % 10 == 0:
        return 1
    return 0


def card_type(number):
    num = int(number[:2])
    l_card = len(number)
    if l_card == 15 and (num == 34 or num == 37):
        print("AMEX")
        return 0
    elif (l_card == 13 or l_card == 16) and 40 <= num < 50:
        print("VISA")
        return 0
    elif l_card == 16 and 50 <= num <= 55:
        print("MASTERCARD")
    else:
        print("INVALID")


while True:
    card = input("Number: ")
    if card.isnumeric():
        break
if lunn_alg(card) == 1:
    card_type(card)
else:
    print("INVALID")
