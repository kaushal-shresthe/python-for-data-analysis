# Write a program to create a billing system at supermarket
while True:
    name = input("Enter customer's name: ")
    total = 0
    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items ? (yes/no): ")
        if repeat.lower() == "no":
            break
    print("="*20)
    print(f"Name: {name}")
    print(f"Total amount: Rs.{total}")
    if total >= 2500:
        print(f"Apply 12% discount: -Rs.{total * 0.12}")
        print(f"Amount to be paid: Rs.{total - total * 0.12}")
    else:
        print(f"Amount to be paid: Rs.{total}")

    print("=" * 20)

    repeat1 = input("Do you want to go to next customer ? (yes/no): ")
    if repeat1.lower() == "no":
        break
