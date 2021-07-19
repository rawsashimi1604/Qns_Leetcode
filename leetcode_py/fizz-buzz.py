class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = []
        for i in range(n):
            if (i + 1) % 5 == 0 and (i + 1) % 3 == 0:
                output.append("FizzBuzz")

            elif (i + 1) % 3 == 0:
                output.append("Fizz")

            elif (i + 1) % 5 == 0:
                output.append("Buzz")

            else:
                output.append(str(i+1))

        return output
