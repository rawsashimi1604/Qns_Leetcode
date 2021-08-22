class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        
        # Add to hashmap, number as key, val as index 
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        # Iterate through arr, find difference, cmp to hashmap
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap and hashmap[diff] != i:
                return[i, hashmap[diff]]
            
            else:
                diff = 0
        
        return []
            
        
                