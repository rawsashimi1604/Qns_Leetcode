import math


def solution(n):
    # Mod by the integer by 10
    # store the remainder, that is the first digit
    # Then - remainder then divide by 10
    # Repeat until number < 10

    output = ""
    while (n != 0):
        remainder = n % 10
        output += str(remainder)
        n = math.floor((n - remainder) / 10)

        print(n)
        print(output)

    return int(output)
