
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


#write a program that ask for the name of a patient and also asks the age, then it will calculate the age of a person and display a message "the Patient " + Name + " is of age." or " is underage."

name = input("Please enter the patient's name: ")
age = int(input("Please enter the patient's age: "))
# #We use the int() function to convert the age input to an integer
if age >= 18:
    print("The patient " + name + " is of age.")
else:
    print("The patient " + name + " is underage.")

    #Write a function that will add all numbers greater or equal to 10 from a list of numbers
def add_numbers_greater_than_or_equal_to_10(numbers):
     total = 0
     for num in numbers:
        if num >= 10:
            total += num
     return total
numbers = [5, 10, 15, 20, 25]
total = add_numbers_greater_than_or_equal_to_10(numbers)
print("The total of all numbers greater than or equal to 10 is:", total)
