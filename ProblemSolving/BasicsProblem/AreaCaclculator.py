# Write a program to create Area Calculator

print("\t\t\t\tArea Calculator\t\t\t\t")
print(
    """
    Press 1 to calculate area of Triangle
    Press 2 to calculate area of Square
    Press 3 to calculate area of Rectangle
    Press 4 to calculate area of Circle
    """)

while True:
    option = int(input("Press (1 - 4) to calculate area: "))

    if option == 1:
        base = float(input("Enter the base of Triangle: "))
        height = float(input("Enter the height of Triangle: "))
        print(f"Area of Triangle = {(base * height) / 2}")

    elif option == 2:
        side = float(input("Enter the side of Square: "))
        print(f"Area of Square = {side ** 2}")

    elif option == 3:
        length = float(input("Enter the length of Rectangle: "))
        width = float(input("Enter the width of Rectangle: "))
        print(f"Area of Rectangle = {length * width}")

    elif option == 4:
        radius = float(input("Enter the radius of Circle: "))
        pi = 22 / 7
        print(f"Area of Circle = {pi * (radius ** 2)}")

    else:
        print("Invalid input. Please enter a number from 1 to 4.")
        continue

    confirmation = input("Do you want to exit? (y/n): ").lower()
    if confirmation == "y":
        break
