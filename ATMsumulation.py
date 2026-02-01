bank = { 
    "aditi" : 95454,
    "naman" : 89878,
    "randy" : 65256,
    "john"  : 31218,
    "pandat" : 31982,
    "gadariya":56512,
    "mohit"  : 28879
}
person = input("Enter your name: ")
while True:
    action = input("Choose an action (check balance, deposit, withdraw, exit): ")
    if action == "check balance":
        print(f"Your current balance is: ${balance}")
    elif action == "deposit":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited. New balance is: ${balance}")
        else:
            print("Invalid deposit amount.")
    elif action == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn. New balance is: ${balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    elif action == "exit":
        print("Exiting the ATM simulation. Goodbye!")
        break
    else:
        print("Invalid action. Please try again.")


