from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            if hashmap.get(nums[i]):
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        for key in hashmap:
            if hashmap[key] == 1:
                return key

        return 0
