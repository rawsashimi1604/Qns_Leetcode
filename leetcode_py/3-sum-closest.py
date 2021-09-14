from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)):
            leftPtr = i + 1
            rightPtr = len(nums) - 1
            while leftPtr < rightPtr:
                sumVal = nums[i] + nums[leftPtr] + nums[rightPtr]
                if sumVal == target:
                    return target

                # Get the closest value
                if abs(target - sumVal) < abs(target - closest):
                    closest = sumVal

                if sumVal < target:
                    leftPtr += 1

                else:
                    rightPtr -= 1

        return closest
