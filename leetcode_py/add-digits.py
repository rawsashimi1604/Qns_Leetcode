class Solution:
    def addDigits(self, num: int) -> int:
        # Using Digital Root
        return num if num == 0 else num % 9 or 9
