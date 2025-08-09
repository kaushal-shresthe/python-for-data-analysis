# Reverse String – Take a string input and write the reversed version of it.
UserInput = input("Enter the string input: ")
Reversed = UserInput[::-1]
print(f"Reversed: {Reversed}")

# Count Vowels and Consonants – Find how many vowels and consonants are in a string.
UserInput = input("Enter the string input: ").lower()
vowels = 0
consonants = 0
for char in UserInput:
    if char == " ":
        continue
    elif char in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

# Check Palindrome – Determine if a string reads the same forwards and backwards.
UserInput = input("Enter the string input: ")
Reversed = UserInput[::-1]
if UserInput == Reversed:
    print(f"{UserInput} is a Palindrome")
else:
    print(f"{UserInput} is not a Palindrome")

# Word Count – Count the number of words in a sentence.
UserInput = input("Enter the string input: ")
words = len(UserInput.split())
print(f"Number of words in a sentence is {words}")


# TODO
# Remove Spaces – Remove all spaces from a string.
# Find Substring – Check if a specific word exists in a string.
# Replace Word – Replace a given word in the string with another word.
# Anagram Check – Check if two strings contain the same characters in any order.
# Character Frequency – Count how many times each character appears in the string.
# Title Case Conversion – Convert a string so that each word starts with a capital letter.
# Find Longest Word – Find the longest word in a sentence.
# Remove Duplicate Characters – Remove repeated characters from a string.
# Check Only Digits – Verify if the string contains only numeric characters.
# Swap Case – Change lowercase letters to uppercase and vice versa.
# Count Special Characters – Count characters that are neither letters nor numbers.
