from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations_dict = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }

        x = 0
        for op in operations:
            op_val = operations_dict[op]
            x += op_val

        return x
