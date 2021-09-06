class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        even_idx = len(s) // 2
        vowels = ['a', 'e', 'i', 'o', 'u']

        s = s.lower()
        firstHalf = s[0:even_idx]
        secondHalf = s[even_idx:]

        firstHalf_v = 0
        secondHalf_v = 0
        for i in range(len(firstHalf)):
            if firstHalf[i] in vowels:
                firstHalf_v += 1

            if secondHalf[i] in vowels:
                secondHalf_v += 1

        return firstHalf_v == secondHalf_v


test = Solution()
print(test.halvesAreAlike("book"))
