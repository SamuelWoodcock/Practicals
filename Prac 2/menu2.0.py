def display_menu():
    print("Menu:")
    print("1. Burger - $5.00")
    print("2. Fries - $2.50")
    print("3. Soda - $1.50")
    print("4. Salad - $4.00")
    print("5. Exit")

def get_item_price(item_number):
    prices = {
        1: 5.00,  # Burger
        2: 2.50,  # Fries
        3: 1.50,  # Soda
        4: 4.00   # Salad
    }
    return prices.get(item_number, 0)

def main():
    total_cost = 0
    while True:
        display_menu()
        try:
            choice = int(input("Select an item (1-5): "))
            if choice == 5:
                break
            quantity = int(input("Enter quantity: "))
            item_price = get_item_price(choice)
            if item_price > 0:
                total_cost += item_price * quantity
                print(f"Added {quantity} of item {choice} to your order.")
            else:
                print("Invalid item selected. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
