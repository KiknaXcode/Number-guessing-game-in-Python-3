import random
import math
# taking lower number input
l = input("Enter Lower bound:- ")
lower = int(l)
 
# taking upper number input
u = input("Enter Upper bound:- ")
upper = int(u)
 
# function that generates random number between these numbers
randomNumber = random.randint(lower, upper) # generates a random integer between lower and upper
print("You have only 10 chances to guess the integer!")
 
# Constant for indicating number of Tries have user
numTries = 10
# variable for counting number of tries
count = 0
 

while numTries > count:
    count += 1
 
    # taking guessing number form user input
    guess = int(input("Guess number:  "))
 
    # check if random number equals to guess
    if randomNumber == guess:
        print("Congratulations, u did it in only", 
              count, "times of try")
        # when user guess number, leave a while loop
        break
    elif randomNumber > guess:
        print("You guess is too small!")
    elif randomNumber < guess:
        print("You Guess is too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= numTries:
    
    print("Losser! Better Luck Next time!")
 
