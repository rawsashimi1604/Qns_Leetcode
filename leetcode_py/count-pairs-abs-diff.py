from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = 0

        for i in range(len(nums)):
            n1 = nums[i]
            for j in range(i + 1, len(nums)):
                if i != j:
                    n2 = nums[j]
                    if abs(n1 - n2) == k:
                        pairs += 1

        return pairs
