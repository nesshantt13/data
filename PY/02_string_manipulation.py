


single_quote = 'Hello'
double_quote = "world"
triple_quote = """Multi line 
asd
asd
asd
string"""


print(single_quote)
print(double_quote)
print(triple_quote)

# # String indexing and slicing
text = "Python Programming"

print(text[0])
print(text[-1])
print(text[0:6])
print(text[:6])
print(text[7:])

# # String methods
name = "bob the builder"

print(len(name))
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("bob", "jane"))

# # String formating
name = "John Doe"
age = 30

message_1 = f"My name is {name} and I am {age} years old."
message_2 = "My name is {} and I am {} years old.".format(name, age)
message_3 = "My name is %s and I am %d years old." % (name, age)

print(message_1)
print(message_2)
print(message_3)

# Exercises :

# 1. Build a simple text analyzer that counts words, characters, and sentences in a given text.
text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use python for web development, data science, and automation. The syntax is clean and readable.
This makes Python  perfect for beginners and experts alike."""

char_count = len(text)
char_count_no_spaces = len(text.replace(" ", ""))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"Character count (including spaces): {char_count}")
print(f"Character count (excluding spaces): {char_count_no_spaces}")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")