import random

choice = ["rock","paper","scissor"]
print("welcome to the rock,paper and scissor game \nchoose your option \n1.rock 2.paper 3.scissor")
user_score = 0
computer_score = 0

while True:
    user_choice = input().lower()
    computer_choice = random.choice(choice)
    print(f"Your choice: {user_choice}\nComputer choice: {computer_choice}")

    if (
        (computer_choice == "rock" and user_choice == "paper")
        or 
        (computer_choice == "paper" and user_choice == "scissor") 
        or 
        (computer_choice == "scissor" and user_choice == "rock")) :
        print("WOW! You win You win")
        user_score += 1
    elif user_choice == computer_choice:
        print("Oops! it's a tie")
    elif user_choice not in choice:
        print("You choose the wrong option \nplease correct right option.")
    else:
        print("Fuck!you lost it")  
        computer_score += 1

    print("Computer score:",computer_score)     
    print("Your score:",user_score)

    play_again = input("Do you want to play more (yes/no):").lower()
    if play_again != "yes":
        print("\n.......Thanks for playing")
        break