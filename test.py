# Python Practice Script

# Variables
name = "John Doe"
age = 30
city = "New York"

# Function to display user details
def display_user_info(name, age, city):
    """Displays a formatted string with user details"""
    print(f"Name: {name}\nAge: {age}\nCity: {city}")

# Function to calculate the square of a number
def square_number(number):
    """Returns the square of a number"""
    return number ** 2

# Function to check if a number is even or odd
def is_even(number):
    """Returns True if the number is even, otherwise False"""
    return number % 2 == 0

# Function to find the factorial of a number
def factorial(n):
    """Returns the factorial of a given number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Execute functions
display_user_info(name, age, city)

num = 5
print(f"The square of {num} is {square_number(num)}")
print(f"Is {num} even? {is_even(num)}")
print(f"Factorial of {num} is {factorial(num)}")
