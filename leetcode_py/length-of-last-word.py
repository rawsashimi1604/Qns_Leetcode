class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == " ":
            return 0
        list_of_words = s.split(" ")
        length = len(list_of_words[-1])
        if length == 0:
            for i in range(1, len(s.split(" ")) + 1):
                if len(list_of_words[-i]) != 0:
                    return len(list_of_words[-i])
            else:
                return 0

        return length  

        

test = Solution()
output = test.lengthOfLastWord("a ")
print(output)