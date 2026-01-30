for i in range(1, 11):
    print(i)

sum = 0
i = 1

while i <= 5:
    sum += i
    i += 1

print("Sum is:", sum)

student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)
