si = int(input())
stk = input().split()

for i in range(si):
     stk[i] = int(stk[i])

stk.sort()

if si%2 == 1:
     print(stk[si//2])

else:
     print(stk[si//2])
     print(stk[(si//2)-1])
     print((stk[(si//2)-1]+stk[si//2])/2)

print(stk)
    