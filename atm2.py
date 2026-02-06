# ATM Simulation Program

bank = {
    "aditi": 95454,
    "madan": 89878,
    "randy": 65526,
    "john": 31218,
    "panda": 31382,
    "gardariya": 56512,
    "mohit": 28879
}

running = True

while running:
    print("\n=== ATM MENU ===")
    todo = input(
        "Open new account or already have account (old / new / exit): "
    ).lower().strip()

    # ---------------- OLD ACCOUNT ----------------
    if todo == "old":
        person = input("Enter your name: ").lower().strip()

        if person in bank:
            print(f"\nWelcome {person.capitalize()}!")

            while True:
                action = input(
                    "\nChoose action (check balance / deposit / withdraw / logout): "
                ).lower().strip()

                if action == "check balance":
                    print(f"💰 Your balance is ₹{bank[person]}")

                elif action == "deposit":
                    amount = float(input("Enter amount to deposit: "))
                    if amount > 0:
                        bank[person] += amount
                        print(f"✅ Deposited ₹{amount}")
                        print(f"💰 New balance: ₹{bank[person]}")
                    else:
                        print("❌ Invalid deposit amount")

                elif action == "withdraw":
                    amount = float(input("Enter amount to withdraw: "))
                    if 0 < amount <= bank[person]:
                        bank[person] -= amount
                        print(f"✅ Withdrawn ₹{amount}")
                        print(f"💰 New balance: ₹{bank[person]}")
                    else:
                        print("❌ Insufficient balance or invalid amount")

                elif action == "logout":
                    print("🔒 Logged out successfully")
                    break

                else:
                    print("❌ Invalid action, try again")

        else:
            print("❌ Account not found. Please register first.")

    # ---------------- NEW ACCOUNT ----------------
    elif todo == "new":
        ac_name = input("Enter your name: ").lower().strip()

        if ac_name in bank:
            print("❌ Account already exists")
        else:
            deposit_money = float(input("Enter initial deposit: "))
            if deposit_money > 0:
                bank[ac_name] = deposit_money
                print("✅ Account created successfully!")
                print("👉 Please login using OLD option")
            else:
                print("❌ Invalid deposit amount")

    # ---------------- EXIT ATM ----------------
    elif todo == "exit":
        print("🙏 Thanks for visiting the ATM")
        running = False

    # ---------------- INVALID ----------------
    else:
        print("❌ Invalid choice, please try again")
