class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                reverseWord = word[0:i+1][::-1]
                remStr = word[i+1:]
                return reverseWord + remStr

        return word
