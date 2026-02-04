import sys
def kandanealgorithem(givenumbers):
    start =0
    end=0
    currsum =0
    maxsum = -sys.maxsize-1 
    n = len(givenumbers)
    while end < n:
        while currsum<0 :
            currsum -= givenumbers[start]
            start +=1   
        currsum += givenumbers[end]
        end +=1

        maxsum = max(maxsum,currsum)
    return maxsum

matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

n = len(matrix)
m = len(matrix[0])  
ans = -sys.maxsize-1

for i in range(m):
    temp = []
    for j in range(n):
        temp.append(matrix[j][i])
    ans = max(ans,kandanealgorithem(temp))

print("Maximum subarray sum is:",ans)