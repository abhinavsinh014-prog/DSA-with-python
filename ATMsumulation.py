bank = { 
    "aditi" : {"balance":95454, "PIN":1234},
    "naman" : {"balance":89878, "PIN":5678},
    "randy" : {"balance":65256, "PIN":9012},
    "john"  : {"balance":31218, "PIN":3456},
    "pandat" : {"balance":31982, "PIN":7890},
    "gadariya":{"balance":56512, "PIN":2345},
    "mohit"  : {"balance":28879, "PIN":4567}
}
running = True
print("======= CHINGI BANK ATM =======")

while running :
    todo = input("Want to open new account or already have account (old/new/exit):-").lower().strip()
    
    if todo == "old" :
        person = input("Enter your name:-").lower().strip()
        
        if person in bank:
            pin  = int(input("Enter your PIN :- "))

            if pin == bank[person]["pin"]:
                print(f"Welcome {person.capitalize()}!")
            
                while True:
                    action = input("Choose an action (check balance, deposit, withdraw, logout): ")
                    
                    if action == "check balance":
                        print(f"Your current balance is: ${bank[person]}")
                    
                    elif action == "deposit":
                        amount = float(input("Enter amount to deposit: "))
                        
                        if amount > 0:
                            bank[person]["balance"] += amount
                            print(f"${amount} deposited.\nNew balance is: ${bank[person]['balance']}")
                        
                        else:
                            print("Invalid deposit amount.")
                    
                    elif action == "withdraw":
                        amount = float(input("Enter amount to withdraw: "))
                        
                        if 0 < amount <= bank[person]["balance"]:
                            bank[person]["balance"] -= amount
                            print(f"${amount} withdrawn.\nNew balance is: ${bank[person]['balance']}")
                        
                        else:
                            print("Invalid withdrawal amount or insufficient funds.")
                    
                    elif action == "logout":
                        print("Exiting the ATM simulation. Goodbye!")
                        break
                    
                    else:
                        print("Invalid action. Please try again!")
            else:
                print("Incorrect PIN. Access denied.")
        else:
            print("Invalid action. Please try again!")
    
    elif todo == "new":
        ac_name = input("Enter your registered name :-").lower().strip()
        
        if ac_name in bank:
            print("account already registered")
        
        else:
            deposit_money = int(input("deposit money :-"))
            pin =int(input("set your 4 digit pin :-"))
            
            if deposit_money > 0:
                bank[ac_name] = {"balance": deposit_money, "pin": pin}
                print("succesfully registered !")
            
            else:
                print("invalid deposit amount.")
    
    elif todo == "exit":
        print("Thanks for visitng")
        running = False
    
    else:
        print("invalid demand !!")