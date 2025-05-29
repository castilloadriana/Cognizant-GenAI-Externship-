import random
number_to_guess = random.randint(1, 100)

num= int(input("Guess the number (between 1 and 100):"))
attempts=1

while num!= number_to_guess:
    if attempts == 10:
        print("Game over! Better luck next time!")
        break 

    if num < number_to_guess:
        print("too low! Try again.")
        num= int(input("Guess the number (between 1 and 100):"))
        attempts+=1
    else:
        print("too high! Try again.")
        num= int(input("Guess the number (between 1 and 100):"))
        attempts+=1

if attempts != 10:
    print("Congratulations! You guessed it in" , attempts, " attempts!")

        


