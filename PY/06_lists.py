# lists and List Operations

fruits = ["banana", "apple", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

# Accessing elements
print(fruits[0])
print(numbers[2])
print(fruits[-1])
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# List Methods
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("banana")
popped = fruits.pop()
fruits.sort()
fruits .reverse()

# List operations
len(fruits)
"apple" in fruits
fruits + ["mango"]
fruits * 2

edited_fruits = fruits.copy()
edited_fruits.append("grape")

#print(edited_fruits)
#print(len(fruits))
print(fruits)
print(popped)

#Exercise

#1. create a grocery list and perform various operations.
shopping_list = ["milk", "bread", "eggs"]

shopping_list.append("butter")
print("After adding:", shopping_list)

shopping_list.remove("bread")
print("After removing:", shopping_list)

#2. Write a program that finds the largest and smallest numbers in a list.
numbers = [10, 5, 8, 3, 12, 7]

print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
print(f"Largest number: {max(numbers)}, Smallest number: {min(numbers)}")

