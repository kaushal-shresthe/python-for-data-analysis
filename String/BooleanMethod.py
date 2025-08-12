# Python String Boolean Methods Example

# 1. isalnum() -> True if all characters are alphanumeric (letters or digits)
text = "abc123"
print(text.isalnum())  # True - all letters and numbers

# 2. isalpha() -> True if all characters are alphabetic
text = "Hello"
print(text.isalpha())  # True - only letters

# 3. isdecimal() -> True if all characters are decimal digits
text = "123"
print(text.isdecimal())  # True - only decimal digits

# 4. isdigit() -> True if all characters are digits (includes superscripts, etc.)
text = "3^2"
print(text.isdigit())  # True - includes superscript ²

# 5. isnumeric() -> True if all characters are numeric (includes fractions, Roman numerals, etc.)
text = "1/3"
print(text.isnumeric())  # True - fraction one-third

# 6. isidentifier() -> True if the string is a valid Python identifier
text = "variable1"
print(text.isidentifier())  # True - valid variable name

# 7. islower() -> True if all cased characters are lowercase
text = "hello"
print(text.islower())  # True - all lowercase

# 8. isupper() -> True if all cased characters are uppercase
text = "HELLO"
print(text.isupper())  # True - all uppercase

# 9. istitle() -> True if string is titlecased
text = "Hello World"
print(text.istitle())  # True - each word starts with uppercase

# 10. isspace() -> True if all characters are whitespace
text = "   "
print(text.isspace())  # True - spaces only

# 11. isprintable() -> True if all characters are printable
text = "Hello!"
print(text.isprintable())  # True - all characters can be printed

# 12. isascii() -> True if all characters are ASCII (Python 3.7+)
text = "Hello"
print(text.isascii())  # True - all ASCII
