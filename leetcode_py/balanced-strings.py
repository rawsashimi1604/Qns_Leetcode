class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        matches = 0
        for char in s:
            if char == "R":
                balance += 1
            elif char == "L":
                balance -= 1
            
            if balance == 0:
                matches += 1
        
        return matches