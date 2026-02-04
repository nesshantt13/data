

name = input("Enter your name: ")
height = float(input("Enter your height in cm: "))

# Input validation
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")

        # Output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")
           

# Exercises :

# 1. Create a simple calculator that takes two numbers and an operator from user.

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                continue
        else:
            print("Invalid operator! Please use one of +, -, *, /.")
            continue

        print(f"The result of {num1} {operator} {num2} is: {result}")
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")


# 2. create a simple quiz program with 3 questions. At the end of the quiz, display score.

score = 0

# # Question 1
answer1 = input("What is the capital of France? ").lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris.")

# # Question 2
answer2 = input("What is 5 + 3? ")
if answer2 == "8":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is 8.")

# # Question 3
answer3 = input("What color do you get when you mix red and blue? ").lower()
if answer3 == "purple":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is purple.")

# Final score
print(f"\nYour final score: {score}/3")
if score == 3:
    print("Perfect score!")
elif score >= 2:
    print("Good job!")
else:
    print("Better luck next time!")