
# Task 1- Counting Down with Loops
# Python program to create a countdown timer.
time= int(input('Give me a timer input for countdown: '))

n= time

while n >= 1:
    print(n)
    n -= 1
print("Blast off! 🚀")

# Task 2 - Multiplication Table with for Loops
# Generates the multiplication table for any number provided by the user
num = int(input("Enter a number: "))
for i in range(11):
    if i == 0:
        continue
    else:
        res= num * i 
        print (num, ' x ', i, ' = ', res)

#Task 3 - Find the Factorial
# Program to calculate the factorial of a number entered by the user
num = int(input("Enter a number: "))
num_res= num

for i in range(num):
    if i == 0:
        continue
    else:
        num_res*= num - i 
print("The factorial of ", num, " is ", num_res)