from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputArr = set()

        for i in range(len(nums)):
            currNum = nums[i]
            leftPtr = 0
            rightPtr = len(nums) - 1

            while (leftPtr < rightPtr):
                if leftPtr == i or rightPtr == i:
                    break

                if currNum + nums[leftPtr] + nums[rightPtr] == 0:
                    outputArr.add(
                        (currNum, nums[leftPtr], nums[rightPtr]))
                    rightPtr -= 1
                    leftPtr += 1

                elif currNum + nums[leftPtr] + nums[rightPtr] > 0:
                    rightPtr -= 1

                else:
                    leftPtr += 1

        # convert set to list
        outputArr = list(outputArr)
        for i in range(len(outputArr)):
            outputArr[i] = list(outputArr[i])
            outputArr[i].sort()

        return outputArr


test = Solution()
test.threeSum([3, 0, -2, -1, 1, 2])
