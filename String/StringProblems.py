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

# Find Longest Word – Find the longest word in a sentence.
# Method 1
text = "Python is beginner friendly language"
longest = ""
start = 0
for i in range(len(text) + 1):
    if i == len(text) or text[i] == " ":
        temp = text[start:i]
        if len(temp) > len(longest):
            longest = temp
        start = i + 1

print(f"Longest word: {longest}")

# Method 2
text = "Python is beginner friendly language"
longest = ""

for word in text.split():
    if len(word) > len(longest):
        longest = word

print(f"Longest word: {longest}")

# Method 2
text = "Python is beginner friendly language"
longest = max(text.split(), key=len)
print(f"Longest word: {longest}")

# Remove Duplicate Characters – Remove repeated characters from a string.
text = "Python is beginner friendly language"
text = text.lower()

result = ""
for i in range(len(text)):
    if text[i] not in result:
        result += text[i]

print("Without duplicates:", result)

# Check Only Digits – Verify if the string contains only numeric characters.
text = "12345"
result = text.isdigit()
if result:
    print("It contains only numeric characters")
else:
    print("It does not contain only numeric characters")

# Swap Case – Change lowercase letters to uppercase and vice versa.
String = "KaUsHaL ShResTHa"
result = ""

for char in String:
    if char.islower():
        result += char.upper()
    else:
        result += char.lower()

print(result)

# Count Special Characters – Count characters that are neither letters nor numbers.
gmail = "KaushalShrestha441@gmail.com ^&*"
count = 0
for char in gmail:
    if char.isalnum() or char.isspace():
        continue
    count = count + 1

print(f"Number of Special Characters: {count}")
