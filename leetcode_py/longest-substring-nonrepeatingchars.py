class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        a_pointer = 0
        b_pointer = 0
        unique_char = []
        maxOutput = 0

        while b_pointer < len(s):
            # Add b pointer until find duplicate character, keep updating max unique characters
            # If found duplicate character, move a pointer, thus sliding the window.
            if s[b_pointer] not in unique_char:
                unique_char.append(s[b_pointer])
                b_pointer += 1
                maxOutput = max(len(unique_char), maxOutput)

            else:
                a_pointer += 1
                unique_char.pop(0)

        return maxOutput
