# This code finds the largest and smallest numbers in a list of numbers.
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

# This code counts the number of even and odd numbers in a list of numbers.
nums = [1, 2, 3, 4, 5, 6, 7]

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

# This code checks if a given number is prime or not.
data = (10, 20, 30, 40, 50)
key = int(input("Enter number: "))

found = False

for item in data:
    if item == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")

# This code finds the common elements between two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common = set()

for i in set1:
    for j in set2:
        if i == j:
            common.add(i)

print("Common elements:", common)


list = [1, 2, 3, 4, 5]
rev = []
for i in range(-1,-len(list)-1,-1):
    rev.append(list[i])
print("Reversed list:", rev)