n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(ops) for ops in input().split()])

for i in range(n):
    for j in range(n):
        if j>i :
            kat = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = kat 
for i in range(n):
    print(matrix[i])