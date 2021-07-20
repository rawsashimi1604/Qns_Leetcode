class Solution:
    def fib(self, n: int) -> int:
        if 0 <= n <= 30:
            if n == 0:
                return 0

            elif n == 1:
                return 1

            else:
                return self.fib(n - 1) + self.fib(n - 2)

        else:
            return 0


test = Solution()
output = test.fib(3)
print(output)
