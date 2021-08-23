from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap = {}
        outStr = ""
        for i in range(len(indices)):
            hashmap[indices[i]] = s[i]
            
        for i in range(len(s)):
            outStr += hashmap[i]
        
        return outStr
            
        