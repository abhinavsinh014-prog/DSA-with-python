si = int(input())
stk = input().split()

for i in range(si):
    stk[i] = int(stk[i])

maxcount = 0
maxma = stk[0]

for cur in stk:
    curcount= 0
    for each in stk:
        if each == cur :
            curcount += 1
        
        if curcount>maxcount :
            maxcount=curcount
            maxma = each

print(maxma,maxcount)

