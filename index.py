
#Write a function that finds a maximum out of 3 different numbers and display the following message: "The greatest number is: " + maxNumber.

def find_max(a, b, c):
    maxNumber = max(a, b, c)
    print("The greatest number is:", maxNumber)

# example usage
find_max(5, 10, 3) # prints "The greatest number is: 10"

def find_max(a, b, c):
    if a >= b and a >= c:
        maxNumber = a
    elif b >= a and b >= c:
        maxNumber = b
    else:
        maxNumber = c
    print("The greatest number is:", maxNumber)

# example usage
find_max(5, 10, 3) # prints "The greatest number is: 10"



