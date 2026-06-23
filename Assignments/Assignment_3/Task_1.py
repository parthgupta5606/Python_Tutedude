def factorial(num):
    if num ==1:
        return 1
    else:
        fact=num*factorial(num-1)
        return fact
    
num=int(input("Enter a number :"))
print(f"factorial of {num} is {factorial(num)}")