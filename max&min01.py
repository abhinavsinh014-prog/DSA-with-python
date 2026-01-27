#To find min and max of list

# tea = list(map(int,input().split()))

# print("min is :-",min(tea))
# print("max is :-",max(tea))

n = int(input())
list = list(map(int,input().split()))

# list = input().split()

# for i in range(n):
#     list[i] = int(list[i])

minel = list[0]
maxel = list[0]

for val in list:
    if val < minel:
        minel  = val
    if val > maxel:
        maxel  = val 

print("min value is :-",minel)   
print("max value is :-",maxel)