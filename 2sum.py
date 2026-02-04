def solve(givenums , target):
    givenums.sort()
    start = 0
    end = len(givenums) - 1
    while start < end:
            currsum = givenums[start] + givenums[end]
            if currsum == target:
                return [givenums[start], givenums[end]]
            elif currsum < target:
                start += 1  
            else:
                end -= 1
    return -1
givenums = [10,2,8,6,7,5,4,3,1,9]
print(solve(givenums, 10))