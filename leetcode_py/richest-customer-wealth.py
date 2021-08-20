class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = float('-inf')
        for customer in accounts:
            if sum(customer) > max:
                max = sum(customer)
                
        return max