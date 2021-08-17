from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if hashmap.get(num):
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        valList = list(hashmap.values())
        keyList = list(hashmap.keys())
        return keyList[valList.index(max(valList))]


test = Solution()
print(test.majorityElement([2, 2, 1, 1, 1, 2, 2]))
