print("Hello World!")

# this is a comment

#VARIABLES
name = "Roland"
last_name = "Hogan"
cohort = 55
is_active = True
print(name + " " + last_name + " #" + str(cohort))
# f-string
print(f"{name.upper()} {last_name} #{cohort}")
print(f"1 + 1 = {1+1}")

# TYPE CONVERSION
num = 9.75
print(type(num))
print(int(num)) # convert a float to an integer

age = 35
print(str(age)) # convert sn integer to a string

price = "10.99"
print(float(price)) # convert a string to a float

#CHALLENGE
# Create some variables called: name,age, and city, show them in a print

city = "Victorville"
print(f"{name} {last_name} {age} {city}")

#Arithmetic Operaation

x = 5
y = 3
print(x + y) # addition
print(x - y)  # subtraction
print(x * y) # multiplication
print(x / y) # division
print(x % y) # modulus
print(x**y) # exponentiation

# COMPARISON OPERATORS
a = 10
b = 5
print(a == b) # equal to
print(a != b) # not equal to
print(a > b) # greater than
print(a < b)  # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

# LOGICAL OPERATORS
x = 5
y = 10
print(x >3 and y < 15) # trsue, both conditions are true
print(x > 3 or y >15) # true, because at least one condition is true
print(not(x>3)) # False, because x is greater than 3 and we are applying not

# LIST
fruits = ["apple", "banana", "cherry", "watermelon"]
print(fruits)
print(fruits[0]) # first element
print(fruits[-1]) # last elements

# LIST METHODS
fruits.append("grape") # add "grape to the list"
print(fruits)

fruits.remove("banana") # removes banana
print(fruits)

print(fruits.pop(1))
print(fruits)

print(fruits.index("grape")) # 
print(fruits)

print(fruits.count("apple"))

print(len(fruits)) # lenght of the list

# IF STATEMENT
# if condition:
        # code to execute if  condition is true


age = 10

if age >= 18:
    print("You are an adult")
else:
    print("you are a minor")

x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# FOR LOOP
fruits = ["apple", "banana", "cherry", "watermelon"]

for fruit in fruits:
    print(fruit)

# (stop), (start, stop), (stop, stop, step)
for i in range(5):
    print(i)

# FUNCTIONS
def greet():
    print("Hello from greet function")

greet() # call the function


# parameters and arguments

def say_hi(name): # name is a parameter
    print("Hi, " + name)
    print(f"Hi, {name}")
    print("Hi,", name)

say_hi("Roland") # Roland is an argument

# DICTIONARY
person = {
    "name": "Roland",
    "age": 38,
    "city": "Victorville",
    "zip": 92305
}

print(person)

print(person["city"])




