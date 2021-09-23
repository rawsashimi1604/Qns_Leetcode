from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            left = 0
            right = len(image[i]) - 1

            # Swap places in array
            while(left < right):
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1

            for j in range(len(image[i])):
                image[i][j] ^= 1

        return image
