from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVal = float('-inf')

        leftPtr = 0
        rightPtr = len(height) - 1

        while(leftPtr < rightPtr):
            minVal = min(height[leftPtr], height[rightPtr])
            maxVal = max(maxVal, minVal * (rightPtr-leftPtr))

            if(height[leftPtr] < height[rightPtr]):
                leftPtr += 1
            else:
                rightPtr -= 1

        return maxVal
