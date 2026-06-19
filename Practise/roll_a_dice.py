import random
print("Welcome to the dice game")
while True:
    choice=input("Press 'Enter' to roll and 'q' to Exit")
    choice=choice.strip()
    if choice=='q':
        print("Thanks for Playing")
        break
    elif choice=='':
        num=random.randint(1,6)
        print(f"Your number is {num}")
    else:
        print("Invalid Choice")

