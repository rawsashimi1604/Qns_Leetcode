class Solution:
    def replaceDigits(self, s: str) -> str:

        output = ""
        for i in range(len(s)):
            if i % 2 == 0:
                output += s[i]

            else:
                val = ord(s[i-1]) + int(s[i])
                if val > 122:
                    val -= 26

                output += chr(val)

        return output


test = Solution()
print(test.replaceDigits("a1c1e1"))
