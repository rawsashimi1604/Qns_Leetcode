from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            
            for j in range(freq):
                decompress.append(val)
        
        return decompress
                       
            