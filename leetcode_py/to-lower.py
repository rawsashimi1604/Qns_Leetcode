class Solution:
    def toLowerCase(self, s: str) -> str:
        newStr = ""
        for char in s:
            # If char is ASCII Upper
            if ord(char) >= 65 and ord(char) <= 90:
                newStr += chr(ord(char) + 32)

            else:
                newStr += char

        return newStr
