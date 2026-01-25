def add(*numbers):
    sum=0
    for num in numbers:
        sum += num
        print(sum)

a , b ,c = int(input()) , int(input()), int(input()) 
add(a,b,c)