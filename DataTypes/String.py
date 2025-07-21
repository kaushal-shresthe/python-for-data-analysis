# Creating Strings
name = 'Kaushal'
msg = "Hello, Python!"
paragraph = '''This is
a multi-line
string.'''


print(name)
print(msg)
print(paragraph)

# String Indexing & Slicing
''' 
 K  a  u  s  h  a  l
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1
'''
text = "Kaushal"
print(text[0])     # K → first character
print(text[-1])    # l → last character
print(text[1:4])   # aus → slicing

# String Functions and Methods

s = "  Hello  Python  "
print(len(s))        #Returns length of the string
print(s.lower())	 #Converts to lowercase
print(s.upper())    #Converts to uppercase
print(s.title())	#First letter capital in each word
print(s.strip())	#Removes whitespace
print(s.replace("Python", "World")) 	#Replaces a with b
print(s.find('o'))	#Returns index of first occurrence
print(s.split())	#Splits string into list (default: space)


#String Concatenation

first = "Hello"
second = "Kaushal"

combined = first + " " + second
print(combined)  # Hello Kaushal


# f-Strings (Formatting)

name = "Kaushal"
age = 18

print(f"My name is {name} and I am {age} years old.")
