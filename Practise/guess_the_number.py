import random

number = random.randint(1, 50)
chances = 10

while chances > 0:
    guess = int(input("Guess the number: "))
    
    if guess == number:
        print("Congratulations! You guessed the number correctly!")
        break
    
    chances -= 1
    
    if guess > number:
        print("Incorrect... Try again! The number is lower.")
    else:
        print("Incorrect... Try again! The number is higher.")
    
    if chances > 0:
        print(f"You have {chances} chances left")
    else:
        print(f"Better luck next time! The number was {number}.")