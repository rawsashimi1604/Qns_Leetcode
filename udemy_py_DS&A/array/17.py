def solution(s1, s2):
    if len(s1) != len(s2):
        return False

    s1Arr = [char.lower() for char in s1]
    s2Arr = [char.lower() for char in s2]

    s1Arr.sort()
    s2Arr.sort()

    for i in range(len(s1Arr)):
        if s1Arr[i] != s2Arr[i]:
            return False
    return True


print(solution('restful', 'fluster'))
