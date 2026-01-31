#write all the even number from 0 to 100 in one line 

# for i in range(0,101,2):
#     print(i,end = " ")

#write all number divide by 7 till 120
# for i in range(7,120,7):
#     print(i) 

#login interface
username = input()
password = input()

data = {
    "aditi" : 1010,
    "naman" : 8958,
    "randy" : 6546,
    "john"  : 3168,
    "pandat" : 3412,
    "gadariya":5612,
    "mohit"  : 2589
}
if username in data:
    if password in data:
        print("wb")
    else:
        print("invp")
else:
    print("inv")