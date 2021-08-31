from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good = 0

        for i in range(len(arr)):
            for j in range(1, len(arr)):
                for k in range(2, len(arr)):
                    if i < j and j < k:
                        if abs(arr[i] - arr[j]) <= a:
                            if abs(arr[j] - arr[k]) <= b:
                                if abs(arr[i] - arr[k]) <= c:
                                    good += 1

        return good
