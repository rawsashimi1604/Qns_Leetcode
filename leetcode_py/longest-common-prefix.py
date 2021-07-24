from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Sort strings so that we can use the smallest and largest string, wont have index errors.
        strs.sort()

        # Iterate through all shortest and longest string.
        for i in range(len(strs[0])):

            # If the word up to i prefix does not match, return the word up to that prefix.
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]

        # Else every word matches
        return strs[0]


test = Solution()
output = test.longestCommonPrefix(['cario', 'carry', 'carracer', 'd'])
print(type(output))
