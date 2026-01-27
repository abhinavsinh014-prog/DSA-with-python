n = int(input())
m = int(input())

grid = []
for i in range(n):
    elen = [int(ele) for ele in input().split()]
    grid.append(elen)
# for i in range(n):
#     ele = input().split()
#     for j in range(m):
#         ele[j] = int(ele[j])
#     grid.append(ele)
print(grid)