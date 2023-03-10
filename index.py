
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


#Write a function that will show the inverse version of a given string. Example: given string "hola" reverse string "aloh".
def reverse_string(string):
    return string[::-1]
string = "mahtab"

inverse_string = reverse_string(string)
print("The inverse version of the string is:", inverse_string)


#write a function that will divide 2 numbers, use an anonymous function for this. And display a message with the result. num1/num2

def divide_numbers(num1, num2):
    result = (lambda x, y: x / y)(num1, num2)
    print("The result of dividing", num1, "by", num2, "is:", result)
num1 = 10
num2 = 5
divide_numbers(num1, num2)



#write a program that will count the number of letters "a" in a string, after show the following message "The number of iterations of letter A is: " + counterA.

string = input("Enter a string: ")

counterA = 0
for char in string:
    if char == "a" or char == "A":
        counterA += 1

print("The number of iterations of letter A is:", counterA)


#write a function that will fin the minimum of 3 numbers and display the following message "The smallest number is: " + maxNumber.

def find_smallest(num1, num2, num3):
    smallest = min(num1, num2, num3)
    print("The smallest number is:", smallest)

num1 = 10
num2 = 5
num3 = 7
find_smallest(num1, num2, num3)

#Write a function that given a list of numbers, it will return new list of numbers only displaying one time each element. Example: list (1,1,1,2,2,3,3,5,6) new list (1,2,3,5,6)

def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers


numbers = [1, 1, 1, 2, 2, 3, 3, 5, 6]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)


#Write a function that given a list of numbers, it will generate two new lists of numbers, one with the odd numbers and one with the even numbers

def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return odd_numbers, even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers, even_numbers = separate_odd_even(numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

