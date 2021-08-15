def solution(nums):
    hashmap = {}
    for i in range(len(nums)):
        if hashmap.get(nums[i]):
            hashmap[nums[i]] += 1
        else:
            hashmap[nums[i]] = 1

    listKeys = list(hashmap.keys())
    duplicates = []
    for n in listKeys:
        if hashmap[n] > 1:
            duplicates.append(n)

    return duplicates


print(solution([1, 1, 1, 1, 2, 2, 23, 21, 22, 23]))
