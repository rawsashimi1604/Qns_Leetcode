from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get product of every value of left
        leftArr = [1]
        leftVal = 1
        for i in range(1, len(nums)):
            leftVal *= nums[i-1]
            leftArr.append(leftVal)

        # Get product of every value of right
        rightArr = [1]
        rightVal = 1
        for i in range(len(nums) - 2, -1, -1):
            rightVal *= nums[i+1]
            rightArr.append(rightVal)

        rightArr.reverse()

        outputArr = []
        for i in range(len(nums)):
            outputArr.append(rightArr[i] * leftArr[i])

        return outputArr


test = Solution()
print(test.productExceptSelf([1, 2, 3, 4]))
# [24,12,8,6]
