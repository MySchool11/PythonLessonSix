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
    print("Nevermind none of the choices right now are any good")