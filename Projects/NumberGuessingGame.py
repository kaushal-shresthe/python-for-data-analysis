import random
while True:
    num = random.randint(1, 100)
    count = 0
    while True:
        user_input = int(input("Guess the number: "))
        count = count + 1
        if user_input == num:
            print(f"you got it and you take {count} attempt ")
            break
        elif user_input > num:
            print("High")
        else:
            print("low")

    repeat = input("Do want to play again? (yes/no): ")
    if repeat.lower() == "no":
        break

