from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Sort from lowest len to highest len
        words.sort(key=lambda x: len(x))
        letterDict = {letter: words[0].count(letter) for letter in words[0]}

        for letter in letterDict.keys():
            for word in words[1:]:
                tmpCount = word.count(letter)

                # Word not found, remove from dict
                if tmpCount == 0:
                    letterDict[letter] = 0
                    break

                # If letterDict contains more than common letters, reduce it to the common letters
                if tmpCount < letterDict[letter]:
                    letterDict[letter] = tmpCount

        outList = []
        for key in letterDict.keys():
            if letterDict[key] > 0:
                for i in range(letterDict[key]):
                    outList.append(key)

        return outList
