from datetime import date

year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't come yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth_date = date(year, month, day)
age = calculate_age(birth_date)

print(f"Your age is: {age} years")
