# Creating a range object from 0 to 9 (10 is not included)
numbers = range(0, 10)

# Print the range object and its type (it's a range object, not a list)
print(numbers, type(numbers))

# Convert the range object to a list to display its contents
numbers = list(numbers)

# Print the list of numbers and its type
print(numbers, type(numbers))

# Loop through numbers from 0 to 9 and print each number
for i in range(10):
    print(i)

# Create a list of letters
letters = ['a', 'b', 'c']

# Loop through each letter in the list and print it
for letter in letters:
    print(letter)

# Loop through a manually defined list of numbers and print each number
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)

# Using ord() to get the Unicode code point of the character 'A'
print('A', ord('A'))

# Using chr() to get the character represented by the Unicode code point 33
print(33, chr(33))

# Using chr() to get the character represented by the Unicode code point 100
print(100, chr(100))

# Additional cool examples:

# Using ord() and chr() to print the alphabet
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=' ')  # Print characters from 'a' to 'z'

print()  # Newline for better formatting

# Printing ASCII values for uppercase letters
for i in range(ord('A'), ord('Z') + 1):
    print(f"{chr(i)}: {i}")  # Print each uppercase letter and its ASCII value

# Demonstrating the use of step in range() to print even numbers
for i in range(0, 21, 2):  # Start at 0, end at 20, and step by 2
    print(i, end=' ')  # Print even numbers from 0 to 20

print()  # Newline for better formatting

# Demonstrating reverse range by stepping backward
for i in range(10, 0, -1):  # Start at 10 and count down to 1
    print(i, end=' ')  # Print numbers from 10 to 1
