
# Factorial Function: recursive function to calculate the factorial of a number and display the result.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num - 1)

# Fibonacci Function: recursive function to calculate the nth Fibonacci number and display the result.
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


#Call: program that presents a menu of choices and performs that task: Calculate the factorial of a number, Find the nth Fibonacci number, Exit.
#The user should select an option by entering a number.
# Returns the result or asks for clarity

def call():
    user_input= int(input("Welcome to the Recursive Artistry Program! Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Exit "))

    if (user_input == 1):
        num = int(input("Enter a number to find its factorial: "))
        print(f"The factorial of {num} is {factorial(num)}")

    elif (user_input == 2):
        num = int(input("Enter a number to find its fibonacci number: "))
        print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
    elif (user_input == 3):
        print("Goodbye!")
        exit
    else:
        print("Choose an option from 1-3")
        call()

call()