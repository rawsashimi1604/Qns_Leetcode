from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]

        number = 0
        for i in range(len(gain)):
            number += gain[i]
            altitudes.append(number)

        return max(altitudes)
