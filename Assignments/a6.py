# Task 1 - Understanding Python Exceptions
# Prompts the user to enter a number, tries to divide 100 by the number, 
# handles ZeroDivisionError AND ValueError exceptions
inpt= int(input("Enter a number: "))
try: 
    print(f"100 divided by {inpt} is {100 / inpt}" )

except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")

except ValueError:
    print("Invalid input!")


# Task 2 - Types of Exceptions
# Program that intentionally raises and handles IndexError, KeyError, TypeError exceptions.
try:
    lst= [1, 2, 3, 4]

    lst[4]= 5
except IndexError: 
    print("IndexError occurred! List index out of range.")

try:
    fruits= {"apple": 1, "berry": 8}
    fruits["melon"]=8
except:
    print("KeyError occurred! Key not found in the dictionary. ")

try:
    result= "adriana" + 8
except:
    print("TypeError occurred! Unsupported operand types.")

# Task 3 - Using try...except...else...finally
# Prompts the user to enter two number, tries to divide the first number by the second number
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result= num1/num2

except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")

except ValueError:
    print("Invalid input!")

else:
    print(f"The result is {result}.")

finally:
    print("This block always executes.")
