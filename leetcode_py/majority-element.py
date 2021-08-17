from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if hashmap.get(num):
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        n = len(nums)
        valList = list(hashmap.values())
        keyList = list(hashmap.keys())

        for i in range(n):
            if valList[i] > n/2:
                return keyList[i]

        return -1


test = Solution()
print(test.majorityElement([2, 2, 1, 1, 1, 2, 2]))
