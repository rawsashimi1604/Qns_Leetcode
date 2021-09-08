class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.casefold() for char in s if char.isalnum()])
        return s == s[::-1]
