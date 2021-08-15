def solution(nums):
    startPointer, endPointer = 0, len(nums) - 1
    while (startPointer < endPointer):
        nums[startPointer], nums[endPointer] = nums[endPointer], nums[startPointer]
        startPointer += 1
        endPointer -= 1

    return nums


print(solution([1, 2, 3, 4, 5]))
