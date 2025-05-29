age = int(input("How old are you? "))

#This conditional checks if the age is 18 or above, if so it gives permission to vote 
if age >= 18: 
    print("Congratulations! You are eligible to vote. Go make a difference!")

#If the users entered age is not 18, the get a response that details the years they have to wait to be elligible for voting 
else:
    x= 18 - age
    print("Oops! You’re not eligible yet. But hey, only", x , " more years to go!")