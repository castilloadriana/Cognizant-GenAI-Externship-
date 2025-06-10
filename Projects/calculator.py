# Python calculator that gracefully handles exceptions and provides
# helpful feedback to users. Menu of the following operations: 
# Addition, Subtraction, Multiplication, Division, Exit


print("Welcome to the Error-Free Calculator!")

try:
    operation= int(input(" 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit > "))

    while (operation > 5):
        print("Choose a menu item option from 1-5")
        operation= int(input(" 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit > "))

except ValueError:
    print("Invalid input! Please enter a valid number.")

else: 
    if(operation == 5): 
        exit()
        
    else :
        try:
            num1= int(input("Enter the first number: "))
            num2= int(input("Enter the second number:"))

        except ValueError:
            
            print("Invalid input! Please enter a valid number.")

        else:   
            if (operation == 1):
                print(num1+num2)
        
            elif (operation == 2):
                print(num1-num2)

            elif (operation == 3):
                print(num1*num2)
            
            elif (operation == 4):
                try:
                    print(num1/num2)

                except ZeroDivisionError:
                    print("Oops! Division by zero is not allowed.")


finally:
    print("Goodbye")
