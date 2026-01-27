si = int(input())
stk = input().split()
starksum = 0
for i in range(si):
    starksum += int(stk[i])
l = len(stk)
print(starksum/l)