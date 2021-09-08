from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Set profit to 0
        prof = 0
        buy = prices[0]

        for num in prices:
            # if current iteration is less than first, set current iteration to buyprice
            if num < buy:
                buy = num

            # if current iteration - buyprice > profit, set that as profit
            if num - buy > prof:
                prof = num - buy
        return prof
