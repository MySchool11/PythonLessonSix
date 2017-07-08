__author__ = "Mr Bancroft"

# Python does not use a delimiter (symbol to identify the line end), instead it relies on correctly structuring the code
# using indentations to show where related code is
for i in range(1, 12):
    print("i = {:3}".format(i))
    print("i * 2 = {:3}".format(i * 2))
    print("i * i (i squared) = {:3}".format(i ** 2) + "\n")
print("\nLoop finished")

# using the above block as an example, everything in the for loop is indented and everything outside of it is not run in
# the loop hence the final print() statement runs only once

# flow can be controlled by ordering your statements correctly, if we want to ask the user their age, first we need
# their name
name = input("Please enter your name: ")
age = int(input("Please enter your age {0}: ".format(name)))
print("{0}, your age is {1}, correct?".format(name, age))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You will have to wait {0} more years to vote yet".format(18 - age))

# you can also use elif which is short for "else if"

print("Please guess a number between 1 and 10")
guess = int(input())
# first if statement in first loop tests whether guess is less than five
if guess < 5:
    print("Please guess higher")
    guess = int(input())
    # if in second loop tests whether the second guess was equal to (==) five
    if guess == 5:
        print("Well done, you guessed it")
    # else in second loop prints sorry message as guess != (not equal to) five, so is incorrect
    else:
        print("Sorry, you guessed incorrectly")
# second elif statement in first loop tests whether guess is more than five
elif guess > 5:
    print("Press guess lower")
    guess = int(input())
    # if in third loop tests whether the second guess was equal to five
    if guess == 5:
        print("Well done, you guessed it")
    # else in third loop prints sorry message as guess != five, so is incorrect
    else:
        print("Sorry, you guessed incorrectly")
# final else statement in first loop will display well done as if the guess is not <5 or >5 it must be 5
else:
    print("Well done, you got it first time!")
# If you are struggling to comprehend this loop, please see the attached flow chart
########################################################################################################################
# We can, however, make this whole loop a lot simpler
guess = int(input("Please guess a number between 1 and 10: "))
if guess != 5:
    if guess < 5:
        guess = int(input("Please guess higher: "))
    else:
        guess = int(input("Please guess lower: "))
    if guess == 5:
        print("Well done, you guessed it.")
    else:
        print("Sorry, you did not guess it.")
else:
    print("well done, you guessed it first time!")
# see - 12 lines as opposed to the original 18 and the level of repetition is much less - a really important goal in
# programming (remember being dry is better than being wet, Don't Repeat Yourself is better than Writing Everything
# Twice)
########################################################################################################################
