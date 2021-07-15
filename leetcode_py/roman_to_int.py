class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0

        romanDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for i in range(0, len(s)):
            if i != len(s) - 1:
                if romanDict[s[i]] > romanDict[s[i+1]]:
                    output += romanDict[s[i]]

                elif romanDict[s[i]] < romanDict[s[i+1]]:
                    output -= romanDict[s[i]]

                else:
                    output += romanDict[s[i]]

            else:
                output += romanDict[s[i]]
        
        return output

test = Solution()
output = test.romanToInt("MCMXCIV")
print(output)