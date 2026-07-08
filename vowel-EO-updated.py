# Input
user_string = input("Enter a string: ")

# 1. Reverse the string (using slicing)
reversed_string = user_string[::-1]

# 2. Count vowels (case-insensitive)
vowel_count = (
    user_string.lower().count('a') + 
    user_string.lower().count('e') + 
    user_string.lower().count('i') + 
    user_string.lower().count('o') + 
    user_string.lower().count('u')
)

# Output
print("Reversed string:", reversed_string)
print("Number of vowels:", vowel_count)


#Question No.2 Checking odd or even
# Input
num = int(input("Enter a number: "))

# Even/Odd check
result = "Even" if num % 2 == 0 else "Odd"

# Output
print(f"The number {num} is {result}.")