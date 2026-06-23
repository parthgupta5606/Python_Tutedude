balance=0

def checkbalance():
    print("Checking Balance...")
    print(f"Your current balance is :Rs.{balance}/-")

def withdraw():
    global balance
    amount=int(input("Enter amount to be withdrawn"))
    if amount<0:
        print("Invalid Amount entered")
    elif amount>balance:
        print("Insufficient Balance !!!")
    else:
        balance-=amount
        print("Amount withdrawn successfully !!")

def deposit():
    global balance
    money=int(input("Enter amount to be deposited"))
    if money<0:
        print("Invalid amount entered")
    else:
        balance=balance+money
        print("Amount deposited successfully")

print("Welcome to ABC Banking !!!")

while True:
    print("Choose from the options below:")
    print("1.Check Balance")
    print("2.Withdraw Money")
    print("3.Deposit Money")
    print("4.Quit")
    choice=int(input("Enter your choice(1-4) :"))

    if choice == 1:
        checkbalance()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        deposit()
    elif choice == 4:
        break
    else:
        print("Invalid Choice")

print("Thanks for using ABC Banking")