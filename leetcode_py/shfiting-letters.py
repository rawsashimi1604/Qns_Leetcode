from typing import List


class Solution:
    def __init__(self):
        self.shifts = []
        self.sum = 0

    def shift(self, char, index):
        # Get the sum, do from start
        char = ord(char) - 97 + self.sum
        char %= 26
        char += 97

        # Minus the current index shift
        self.sum -= self.shifts[index]

        return chr(char)

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:

        # "abc", [3,5,9], sum = 17
        self.shifts = shifts
        self.sum = sum(shifts)

        outStr = ""
        for i in range(len(S)):
            outStr += self.shift(S[i], i)

        return outStr
