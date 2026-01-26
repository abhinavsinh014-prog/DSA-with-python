list1 = [1,5,8,6,4,2,3]
print("Normal list",list1)

list1.append(7) #adding a number with append
print("after append",list1)

list1.insert(5,9)
print("after insert",list1)

list1.pop(4)
print("after pop",list1)

dam = list1.pop(4)
print(dam)