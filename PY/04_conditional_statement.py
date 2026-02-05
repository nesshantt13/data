# Conditional Statements

# Fundamental conditional statements
age = 25

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# # Multiple conditional statements
score = 85

if score >= 90:
    grade = "A"
elif score >= 80: 
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# # 'and' : Both conditions must be True.
user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")

































# Exercise:

#1. Write a program that categorizes BMI (Body Mass Index) into underweight(<18.5), normal weight(<24.9), overweight(<29.9), and 
# obesity(>30.0).(formula = kg/m^2)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 24.9:
    category = "normal weight"
elif bmi < 29.9:
    category = "overweight"
else:
    category = "obesity"

print(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")


# BMI Calculator (height in cm)

# Weight input
while True:
    weight = float(input("Enter your weight (kg): "))
    if weight > 0 and weight < 300:
        break
    else:
        print("Please insert valid value! (0-300kg)")

# Height input in cm
while True:
    height_cm = float(input("Enter your height (cm): "))
    if height_cm > 0 and height_cm < 200:
        break
    else:
        print("Please insert valid value! (0cm-200cm)")

# Convert cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

print("Your BMI is:", round(bmi, 2))

# Categorize BMI
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")

    