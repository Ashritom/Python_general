def ATM():
    balance = 0
    
    while True:
        print("Welcome !!")
        print("Please select an option from the following list:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")
        
        x = int(input("Enter your choice: "))
        
        if x == 1:
            amount = float(input("Enter the amount that you want to deposit: "))
            balance += amount
            print("Balance =", balance)
        elif x == 2:
            amount = float(input("Enter the amount that you want to withdraw: "))
            if balance >= amount:
                balance -= amount
                print("Balance =", balance)
            else:
                print("Insufficient balance")
        elif x == 3:
            print("Balance =", balance)
        elif x == 4:
            print("Exit successful!")
            break
        else:
            print("Invalid choice")

def main():
    pin = 4562
    
    while True:
        PIN = int(input("Please Enter your pin: "))
        if PIN == pin:
            ATM()
        else:
            print("ERROR !!!\nPlease enter a valid pin")
        
        user_input = input("Do you want to continue? (yes/no): ")
        if user_input.lower() == "no":
            break

main()
