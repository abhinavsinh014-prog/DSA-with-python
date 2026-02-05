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
