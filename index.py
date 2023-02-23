
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

#Write a function that adds minimum 2 numbers but can add more if needed, display the following message: "The total is: " + total. (use Variable-length Arguments)


def add_numbers(*args):
    total = sum(args)
    print("The total is:", total)
add_numbers(2, 4)  # Output: The total is: 6
add_numbers(1, 3, 5, 7)  
add_numbers(-10, 0, 10, 20, 30)  
#another way of doing it without using sum function
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("The total is:", total)

add_numbers(2, 4)