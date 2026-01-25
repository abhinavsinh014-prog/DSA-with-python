n = 69
for i in range(1,n+1):
    temp = i

    while temp%3==0:
        temp/= 3

    if temp == 1:
        continue
    print(i)    
    
 