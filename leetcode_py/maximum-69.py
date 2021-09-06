class Solution:
    def maximum69Number(self, num: int) -> int:

        res = [num]
        arr = [int(x) for x in str(num)]

        for i in range(len(arr)):
            arr = [int(x) for x in str(num)]
            tmp = ""
            if arr[i] == 6:
                arr[i] = 9
            else:
                arr[i] = 6

            for j in range(len(arr)):
                tmp += str(arr[j])

            res.append(int(tmp))

        return max(res)


test = Solution()
test.maximum69Number(9669)
