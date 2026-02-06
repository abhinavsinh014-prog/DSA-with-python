bank = { 
    "aditi" : 95454,
    "naman" : 89878,
    "randy" : 65256,
    "john"  : 31218,
    "pandat" : 31982,
    "gadariya":56512,
    "mohit"  : 28879
}
todo = input("Want to open new account or already have account (old/new):-")
if todo != "new" :
    person = input("Enter your name: ")
    if person in bank:
        while True:
            action = input("Choose an action (check balance, deposit, withdraw, exit): ")
            if action == "check balance":
                print(f"Your current balance is: ${bank[person]}")
            elif action == "deposit":
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    bank[person] += amount
                    print(f"${amount} deposited. New balance is: ${bank[person]}")
                else:
                    print("Invalid deposit amount.")
            elif action == "withdraw":
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= bank[person]:
                    bank[person] -= amount
                    print(f"${amount} withdrawn. New balance is: ${bank[person]}")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")
            elif action == "exit":
                print("Exiting the ATM simulation. Goodbye!")
                break
            else:
                print("Invalid action. Please try again!")
else:
    ac_name = input("enter your name :-")
    deposit_money = int(input("deposit money :-"))
    bank[ac_name] = deposit_money
    print("succesfully registered !")