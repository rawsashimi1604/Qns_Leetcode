from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        lengths = []

        for i in range(len(rectangles)):
            lengths.append(min(rectangles[i]))

        maxLength = max(lengths)
        counter = 0
        for i in range(len(lengths)):
            if lengths[i] == maxLength:
                counter += 1

        return counter
