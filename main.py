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