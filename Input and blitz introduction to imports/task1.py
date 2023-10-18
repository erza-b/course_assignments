#Task 1

#The Guessing Game.

#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
#The result should be sent back to the user via a print statement.

import random

random_number = random.randint(1, 10)
user_guess = int(input("Sheno nje numer 1-10 "))

if user_guess == random_number:
    print("Numri i sakte")
else:
    print(f"Na vjen keq,numri i sakte eshte {random_number}.")

