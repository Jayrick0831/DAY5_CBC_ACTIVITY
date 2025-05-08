@@ -0,0 +1,27 @@
balance = 100000

while True:
    transaction = input("Type \n 1 (deposit)\n 2 (withdraw)\n 3 (view balance)\n 0 (quit)\n: ")

    if transaction == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposited: ₱{amount:,.2f}")

    elif transaction == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdraw: ₱{amount:,.2f}")
        else:
            print("NO BALANCE!")

    elif transaction == "3":
        print(f"Current balance: ₱{balance:,.2f}")

    elif transaction == "0":
        print("Thank you for Banking!")
        break

    else:
        print("Try Again!")
