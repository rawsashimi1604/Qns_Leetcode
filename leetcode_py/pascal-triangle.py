from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # end array and start array is always 1
        # len of array = rowN
        outputList = [[] for i in range(numRows)]
        outputList[0] = [1]
        n = numRows
        rowIdx = 0
        while n > 1:
            rowIdx += 1
            currArr = [0 for i in range(rowIdx + 1)]
            currArr[0], currArr[-1] = 1, 1
            for j in range(rowIdx - 1):
                currArr[j+1] = outputList[rowIdx-1][j] + outputList[rowIdx-1][j+1]

            outputList[rowIdx] = currArr
            n -= 1

        return outputList
test = Solution()
print(test.generate(5))