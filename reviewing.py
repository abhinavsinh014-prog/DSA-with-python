print("Welcome to reviewing system")
rating = float(input("Rate this product out of 5 :-"))
if rating>=5:
    print("invalid rating")
else:
    print("Thanks for your rating")
comment = input("Any comments on product:-")
print("Thanks for your comment")

anything_else = input("anything else (complain/query) :-")
if anything_else == "query":
    print(input("ask your query "))
    print(input("we connect to you for your query8"))
if anything_else == "complain":
    print(input("told us your complain"))
    print("sorry for this mistake")