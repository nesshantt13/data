

# Basic class definition
class Person:
# Class attribute (shared by all instances)
    species = "Homo sapiens"

    # Constructor method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

        # Instance method
    def introduce(self):
        return f"Hi, Im {self.name}, and I am {self.age} years old."
    
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! is now {self.age}."
        
# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)
print(person1.age)

# Calling methods
print(person1.introduce())
print(person1.have_birthday())

# Class attributes
print(Person.species)
print(person1.species)




class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."
        
    def get_balance(self):
        return f"Current balance: ${self.balance}"
    
    def get_transaction_history(self):
        return self.transaction_history
    
    # Using the BankAccount class
account = BankAccount("12345", "Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

 #Exercise   
 # 1. create a simple game character class with health, attack, and heal methods.

# 1. Create a simple game character class with health, attack and defend methods
class GameCharacter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.max_health = health
    
    def attack(self, target):
        damage = 20
        target.health -= damage
        if target.health < 0:
            target.health = 0
        return f"{self.name} attacks {target.name} for {damage} damage!"
    
    def defend(self):
        heal_amount = 10
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        return f"{self.name} defends and heals for {heal_amount} HP!"
    
    def is_alive(self):
        return self.health > 0
    
    def status(self):
        return f"{self.name}: {self.health}/{self.max_health} HP"

# Create characters
hero = GameCharacter("Hero", 100)
enemy = GameCharacter("Goblin", 80)

# Game simulation
print("=== BATTLE START ===")
print(hero.status())
print(enemy.status())
print()

# Round 1
print(hero.attack(enemy))
print(enemy.status())
print()

# Round 2
print(enemy.attack(hero))
print(hero.status())
print()

# Round 3
print(hero.defend())
print(hero.status())
print()

# Round 4
print(hero.attack(enemy))
print(enemy.status())
print()

# Check if enemy is still alive
if enemy.is_alive():
    print(f"{enemy.name} is still fighting!")
else:
    print(f"{enemy.name} has been defeated!")
    