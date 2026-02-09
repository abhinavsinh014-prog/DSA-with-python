# # This code finds the largest and smallest numbers in a list of numbers.
# numbers = [12, 45, 7, 89, 23]

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# # This code counts the number of even and odd numbers in a list of numbers.
# nums = [1, 2, 3, 4, 5, 6, 7]

# even = 0
# odd = 0

# for n in nums:
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even)
# print("Odd:", odd)

# # This code checks if a given number is prime or not.
# data = (10, 20, 30, 40, 50)
# key = int(input("Enter number: "))

# found = False

# for item in data:
#     if item == key:
#         found = True
#         break

# if found:
#     print("Element found")
# else:
#     print("Element not found")

# # This code finds the common elements between two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common = set()

for i in set1:
    for j in set2:
        if i == j:
            common.add(i)
print("common",common)
diff = set()
for i in set1:
    found = False
    for j in set2:
        if i==j:
            found = True
            break
    if not found:
        diff.add(i)
print("sum",set1|set2)
print("differnt",diff)
# print("Common elements:", common)

# # This code reverses a list of numbers.
# list = [1, 2, 3, 4, 5]
# rev = []
# for i in range(-1,-len(list)-1,-1):
#     rev.append(list[i])
# print("Reversed list:", rev)

# #given
# n= int(input("Enter number: "))
# i=1
# while i**2<=n:
#     print(i**2,end=" ")
#     i+=1

#for loop
# v = int(input("Enter number: "))
# for i in range(1,11):
#     print(v*i,end=" ")

#fizzbuzz

# p = int(input("Enter number: "))

# if p%3==0 and p%5==0:
#     print("FizzBuzz",end=" ")
# elif p%3==0:
#     print("Fizz",end=" ")
# elif p%5==0:
#     print("Buzz",end=" ")
# else:
#     print(p,end=" ")    

#reverse string

# s = input("Enter string: ")
# for i in range(-1,-len(s)-1,-1):
#     print(s[i],end=" ")

# # 
# arr = [1, 2, 3, 4, 5]
# sum = 9
# found = False
# for i in range(1,len(arr),1):
#     for j in range(1,len(arr),1):
#         if arr[i]+arr[j] == sum:
#             print("pair found",arr[i],arr[j])
#             found = True
#             break
# if found:
#     print("present")
# else:
#     print("absent")     


