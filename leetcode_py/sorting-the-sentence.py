class Solution:
    def sortSentence(self, s: str) -> str:
        strArr = s.split(" ")
        hashmap = {}
        for s in strArr:
            hashmap[int(s[-1])] = s[:-1]

        outputStr = ""
        for i in range(1, len(strArr)+1):
            if i == len(strArr):
                outputStr += hashmap[i]
            else:
                outputStr += hashmap[i] + " "

        return outputStr
