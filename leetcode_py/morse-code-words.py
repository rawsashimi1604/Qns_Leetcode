from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseArr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                    "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        output = set()
        for word in words:
            word_morse = ""
            for char in word:
                word_morse += morseArr[(ord(char) - 97)]

            output.add(word_morse)

        return len(output)
