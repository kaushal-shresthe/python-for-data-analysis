# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects.
# In OOP, programs are designed using classes and objects rather than functions alone.

# Practice
# Q1. Write a Python class called Car with attributes brand and year and a method display() to print car details.
# Create two objects and display their details.

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display(self):
        print(f"Car brand: {self.brand}, Year: {self.year}")


car1 = Car("BMW", 2022)
car2 = Car("Tesla", 2022)

car1.display()
car2.display()


# Q2. Create a Python class called Book with attributes title and author and
# a method show_info() that displays book info.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


book1 = Book("Python", "XYZ")

book1.show_info()

