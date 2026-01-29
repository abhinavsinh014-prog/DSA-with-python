import random

choice = ["rock","paper","scissor"]
user_score = 0
computer_score = 0
print("welcome to the rock,paper and scissor game \nchoose your option between rock, paper and scissor")
user_choice = input().lower()
computer_choice = random.choice(choice)
if (
    (computer_choice == "rock" and user_choice == "paper")
      or 
      (computer_choice == "paper" and user_choice == "scissor") 
      or 
      (computer_choice == "scissor" and user_choice == "rock")) :
    print("WOW! user win")
    user_score += 1
elif user_choice == computer_choice:
    print("Oops! it's a tie")
elif user_choice not in choice:
    print("You choose the wrong option \nplease correct right option.")
else:
    print("Fuck!you lost it")  
    computer_score += 1

print("Computer score",computer_score)     
print("Your score",user_score)