from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        hashmap = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        matches = 0
        
        for item in items:
            if item[hashmap[ruleKey]] == ruleValue:
                matches += 1
                
        return matches