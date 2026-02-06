

# Functions with parameters
def greet_person(name) :
    print(f"Hello, {name}!")

greet_person("Alice")

# Functions with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

# Default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

# *args - variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

# **kwargs - keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# combining *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

    flexible_function(1, 2, 3, name="Alice", age=25)

    # Lambda functions
    square = lambda x: x **2
    print(square(5))

    add = lambda x, y: x + y
    print(add(3, 4))

    #Exercises :
    #1. Write a function that checks if a number is prime.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # True
print(is_prime(4))   # False

# 1. Write a function that checks if a number is prime (lect ans)
def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

# Test the function
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False





#2. Build a temperature converter function. (Celsius to Fahrenheit)

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the functions
print(f"25°C = {celsius_to_fahrenheit(25)}°F")  # 25°C = 77.0°F
print(f"77°F = {fahrenheit_to_celsius(77)}°C")  # 77°F = 25.0°C

# More complete converter with user input
def temperature_converter():
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()
    
    if unit == "C":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result}°F")
    elif unit == "F":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result}°C")
    else:
        print("Invalid unit!")

# Run the converter
temperature_converter()
