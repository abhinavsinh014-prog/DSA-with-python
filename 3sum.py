def solve(givenNums, target):
    temp = givenNums.copy()
    givenNums.sort()

    for k in range(len(givenNums)):
        tempTarget = target - givenNums[k]
        start = k + 1
        end = len(givenNums) - 1

        while start < end:
            currSum = givenNums[start] + givenNums[end]

            if currSum == tempTarget:
                ans = []

                for i in range(len(temp)):
                    if givenNums[start] == temp[i] or givenNums[end] == temp[i]:
                        ans.append(i)

                return ans

            if currSum > target:
                end -= 1
            else:
                start += 1

    return -1