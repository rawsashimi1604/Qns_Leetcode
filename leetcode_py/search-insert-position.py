from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        maxVal = float('-inf')
        if len(nums) == 0:
            return 0
        for num in nums:
            if num > maxVal:
                maxVal = num
            if num == target:
                return idx
            elif maxVal > target:
                return idx
            else:
                idx+=1
                
        return len(nums)