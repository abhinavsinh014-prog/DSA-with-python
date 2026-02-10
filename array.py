from array import *

a1 = array('i',[56,65,24,12])
print(a1)

for x in a1:
    print(x)

for i in range(4):
    print(a1[i],end=",")
print(" ")
c=0
while (c<len(a1)):
    print(a1[c])
    c+=1

a1.append(31)
print(a1)
a1.count(31)
print(a1)
a1.extend([69])
print(a1)
# a1.fromlist(65)
a1.index(31)
print(a1)
a1.pop(1)
print(a1)
a1.reverse()
print(a1)
# a1.tolist()
a1.remove(24)
print(a1)