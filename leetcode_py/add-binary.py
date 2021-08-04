import math

# Convert solution.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Get sum in str
        pwr = len(a)
        a_sum = 0
        for i in range(len(a)):
            a_sum += 2**(pwr-1) * int(a[i])
            pwr -= 1

        pwr = len(b)

        b_sum = 0
        for i in range(len(b)):
            b_sum += 2**(pwr-1) * int(b[i])
            pwr -= 1

        # Convert to binary
        binary_sum = a_sum + b_sum
        binary_list = []
        while (binary_sum/2 >= 1):
            rem = binary_sum % 2
            binary_list.append(rem)
            binary_sum = int(math.floor(binary_sum/2))

        if binary_sum == 1:
            binary_list.append(1)
        else:
            binary_list.append(0)

        binary_list.reverse()
        output = ""
        for digit in binary_list:
            output += str(digit)

        return output


# "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
# "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
