from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get product of every value of left
        leftArr = []
        leftVal = 1
        for i in range(len(nums)):
            if i == 0:
                leftArr.append(1)

            else:
                leftVal *= nums[i-1]
                leftArr.append(leftVal)

        # Get product of every value of right
        rightArr = []
        rightVal = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                rightArr.append(1)
            else:
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
