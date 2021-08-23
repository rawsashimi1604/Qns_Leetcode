class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sumDigits = 0
        digits = [int(digit) for digit in str(n)]
        
        for digit in digits:
            sumDigits += digit
            product *= digit
        
        return product - sumDigits
        
        