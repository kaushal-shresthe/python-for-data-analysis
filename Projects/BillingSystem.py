import datetime

print("========== Welcome to KAUSHAL'S TECH STORE==========\n")
print("Guidelines:")
print("1. Enter item details one by one.")
print("2. Type 1 to enter more items, any other number to stop.\n")

def input_function():
    cart = []
    while True:
        # Input item details with validation
        user_input_name = input("Enter the item name: ").strip()
        if not user_input_name:
            print("Item name cannot be empty. Please enter again.")
            continue
        try:
            user_input_qty = int(input("Enter Quantity: "))
            user_input_price = float(input("Enter Price: "))
            if user_input_qty <= 0 or user_input_price < 0:
                print("Quantity must be positive and price cannot be negative. Try again.")
                continue
        except ValueError:
            print("Invalid input for quantity or price. Please enter numeric values.")
            continue

        calculated_total = user_input_qty * user_input_price
        item = {
            "name": user_input_name,
            "qty": user_input_qty,
            "price": user_input_price,
            "total": calculated_total
        }
        cart.append(item)

        try:
            confirmation = int(input("Do you want add more item? If yes enter 1 otherwise enter any number: "))
        except ValueError:
            print("Invalid input. Exiting item input.")
            break
        if confirmation != 1:
            break
    return cart


def print_bill(cart, customer_name, discount_percent=0, tax_percent=0):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print("\n========== KAUSHAL'S TECH STORE ==========")
    print(f"Customer: {customer_name}")
    print(f"Date: {date_str}")
    print("============================================")
    print(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
    print("--------------------------------------------")

    grand_total = 0
    for item in cart:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        total = item["total"]
        grand_total += total
        print(f"{name:<15}{qty:<10}{price:<10.2f}{total:<10.2f}")

    print("--------------------------------------------")
    print(f"{'Subtotal:':<35}{grand_total:.2f}")

    discount_amount = grand_total * (discount_percent / 100)
    if discount_percent > 0:
        print(f"{'Discount (' + str(discount_percent) + '%):':<35}-{discount_amount:.2f}")

    taxable_amount = grand_total - discount_amount
    tax_amount = taxable_amount * (tax_percent / 100)
    if tax_percent > 0:
        print(f"{'Tax (' + str(tax_percent) + '%):':<35}+{tax_amount:.2f}")

    final_total = taxable_amount + tax_amount
    print(f"{'Grand Total:':<35}{final_total:.2f}")
    print("============================================")
    print("Thank you for shopping with us!\n")
    return final_total, date_str


def save_bill_to_file(cart, customer_name, discount_percent, tax_percent, final_total, date_str):
    filename = f"bill_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("========== KAUSHAL'S TECH STORE ==========\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Date: {date_str}\n")
        f.write("============================================\n")
        f.write(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}\n")
        f.write("--------------------------------------------\n")

        for item in cart:
            f.write(f"{item['name']:<15}{item['qty']:<10}{item['price']:<10.2f}{item['total']:<10.2f}\n")

        grand_total = sum(item['total'] for item in cart)
        f.write("--------------------------------------------\n")
        f.write(f"{'Subtotal:':<35}{grand_total:.2f}\n")

        discount_amount = grand_total * (discount_percent / 100)
        if discount_percent > 0:
            f.write(f"{'Discount (' + str(discount_percent) + '%):':<35}-{discount_amount:.2f}\n")

        taxable_amount = grand_total - discount_amount
        tax_amount = taxable_amount * (tax_percent / 100)
        if tax_percent > 0:
            f.write(f"{'Tax (' + str(tax_percent) + '%):':<35}+{tax_amount:.2f}\n")

        f.write(f"{'Grand Total:':<35}{final_total:.2f}\n")
        f.write("============================================\n")
        f.write("Thank you for shopping with us!\n")

    print(f" Bill saved successfully as '{filename}'\n")


def main():
    while True:
        customer_name = input("Enter customer name: ").strip()
        if not customer_name:
            print("Customer name cannot be empty. Please enter again.")
            continue

        cart = input_function()
        if not cart:
            print("No items entered. Exiting.")
            break

        # Ask for discount and tax percent with validation
        try:
            discount_percent = float(input("Enter discount percentage (0 if none): "))
            tax_percent = float(input("Enter tax percentage (0 if none): "))
            if discount_percent < 0 or tax_percent < 0:
                print("Discount and tax cannot be negative. Setting them to 0.")
                discount_percent = 0
                tax_percent = 0
        except ValueError:
            print("Invalid input for discount or tax. Setting them to 0.")
            discount_percent = 0
            tax_percent = 0

        final_total, date_str = print_bill(cart, customer_name, discount_percent, tax_percent)

        save_choice = input("Do you want to save the bill to a file? (y/n): ").strip().lower()
        if save_choice == 'y':
            save_bill_to_file(cart, customer_name, discount_percent, tax_percent, final_total, date_str)

        cont = input("Do you want to create another bill? (y/n): ").strip().lower()
        if cont != 'y':
            print("Goodbye! Thanks for using KAUSHAL'S TECH STORE billing system.")
            break


if __name__ == "__main__":
    main()
