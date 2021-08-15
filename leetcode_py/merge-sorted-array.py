from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) != 0:
            mIdx = m

            for i in range(n):
                nums1[mIdx] = nums2[i]
                mIdx += 1

            nums1.sort()
        
        else:
            pass