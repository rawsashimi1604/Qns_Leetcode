from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(1, len(arr)+1, 2):
            j = 0
            count = i
            while count <= len(arr):
                total += sum(arr[j:count])
                j += 1
                count += 1

        return total
