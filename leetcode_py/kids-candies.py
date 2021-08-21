from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolArr = [candies[i] + extraCandies >= max(candies) for i in range(len(candies))]
        
        return boolArr