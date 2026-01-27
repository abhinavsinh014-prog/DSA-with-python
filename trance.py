n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(ops) for ops in input().split()])
trance = []
for i in range(n):
    for j in range(n):
        if j == i :
            trance.append(matrix[i][j])
print(trance)