# For and while Loops

# # For Loop
for i in range (5):              # 0, 1, 2, 3, 4
    print(i)

for i in range (1, 6):           # 1, 2, 3, 4, 5
    

    print(i)









# # Exercises:

# # 1. Create a multiplication table generator.
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    

# # 2. Write a program that finds all prime numbers up to a given number.
limit = 20

for num in range(3, limit + 1):
    is_prime = True
    for i in range( 2, num):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(num)