#Task 1 - Writing Functions
# Accepts a name as a parameter and prints a personalized greeting.
# Takes two numbers as parameters, adds them, and returns the result.
def greet_user(name):
    return f"Hello, {name}! Welcome aboard. "

def add_numbers(num1, num2):
    return f"The sum of {num1} and {num2} is  {num1 + num2} "

print( greet_user("Alice"), add_numbers(5, 10))

#Task 2 - Using Default Parameters
# Accepts two parameters AND prints a description of the pet
def describe_pet(pet_name, animal_type):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Muddy", "dog")

#Task 3 - Functions with Variable Arguments
# Accepts a variable number of arguments for sandwich ingredients and prints them as a list.
def make_sandwhich(*arg):
    print("Making a sandwich with the following ingredients: ")
    for i in arg:
        print(f"- {i}")

make_sandwhich("lettuce", "tomato")


#Task 4 - Understanding Recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print(f"The factorial of 5 is {factorial(5)}")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")

