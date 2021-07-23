class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for p in s:
            if p in lookup.values():
                stack.append(p)

            # Must make sure that stack exists, so that there will not be any index errors.
            # Example input : "]" ...
            # p will not be in lookup values, but cannot call stack[-1]
            elif stack and lookup[p] == stack[-1]:
                stack.pop()  # Remove from top of stack

            # If p not in lookup values, means not valid.
            # And if the p did not exist in stack, means it is invalid
            else:
                return False

        return stack == []


test = Solution()
output = test.isValid(']')
print(output)
