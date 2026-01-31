dick = { 
    "aditi" : 954,
    "naman" : 898,
    "randy" : 656,
    "john"  : 318,
    "pandat" : 312,
    "gadariya":512,
    "mohit"  : 289
}

search = input()
if search in dick:
    marks = dick[search]
    percantage = marks/10
    if marks < 333:
        print(" FAIL",)
    else:
        print(" PASS")
    print(f"Name:-{search} Marks:- {dick[search]} percantage:- {percantage}")
else:
    print("student not found")
