myvar = 85

def ufunt(myvar):
    myvar -=3
    print(myvar)

    def u2funt(myvar):
        myvar+=5
        print(myvar)
    
    u2funt(myvar)

print(myvar)
ans = ufunt(myvar)
print(ans)