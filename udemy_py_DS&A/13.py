def solution(s1):
    tmp = [char.lower() for char in s1]
    # reverse tmp
    startPointer = 0
    endPointer = len(tmp) - 1
    while (startPointer < endPointer):
        tmp[startPointer], tmp[endPointer] = tmp[endPointer], tmp[startPointer]
        startPointer += 1
        endPointer -= 1

    if "".join(tmp) == s1.lower():
        return True

    else:
        return False


print(solution("Radar"))
