from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = [0 for i in range(101)]
        # Add to hashmap array
        for i in range(len(nums)):
            smaller[nums[i]] += 1
        
        # Stack up the smaller array
        for i in range(1, len(smaller)):
            smaller[i] += smaller[i-1]
        
        # Get count for each nums
        for i in range(len(nums)):
            position = nums[i]
            if position == 0:
                nums[i] = 0
            else:
                nums[i] = smaller[position - 1]
                
        return nums
                
            
            
        
        
                    
                    
            
            