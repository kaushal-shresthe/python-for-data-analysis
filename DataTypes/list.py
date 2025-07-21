# Accessing List Elements (Indexing & Slicing)

fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])     # apple → first element
print(fruits[-1])    # mango → last element
print(fruits[1:3])   # ['banana', 'cherry']


# List Methods (Commonly Used)

numbers = [3, 1, 4, 2, 3, 4, 2]

numbers.append(5)                     # Adds item at the end
print("After append:", numbers)

numbers.sort()                        # Sorts the list in ascending order
print("After sort:", numbers)

numbers.insert(2, 5)                  # Inserts 5 at index 2
print("After insert:", numbers)

numbers.remove(3)                     # Removes first occurrence of 3
print("After remove:", numbers)

removed_item = numbers.pop(-2)        # Removes second last element
print("Popped item:", removed_item)
print("After pop:", numbers)

numbers.sort()                        # Sorts again
print("After sort again:", numbers)

numbers.reverse()                     # Reverses the list
print("After reverse:", numbers)

copy_list = numbers.copy()            # Copies the list
print("Copied list:", copy_list)

numbers.clear()                       # Removes all items
print("After clear:", numbers)


# 🧠 Important Note:
'''Many list methods like append(), sort(), insert(), remove(), reverse(), and clear() modify the list in-place and 
return None. So:'''
print(numbers.append(5))  # ❌ Wrong → This prints None
# ✅ Instead, call the method first, then print the list.
