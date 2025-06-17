items = {
    "steak": 21,
    "bacon": 5,
    "cheese": 15,
    "rice": 2,
    "fruit bag": 5
}
for item in items:
    print(f"- {item.title()}: ${items[item]}")
print("\nType the item name to add to your cart. Type 'done' when finished.\n")
cart = []
while True:
    # Ask for the item name
    choice = input("Enter item name (or 'done' to finish): ").lower().strip()

    if choice == 'done':
        break

    if choice in items:
        # Ask for the quantity
        quantity = int(input(f"How many {choice}s would you like? "))
        cart.append((choice, quantity))

        print(f"Added {quantity} x {choice} to your cart.")
    else:
        print("Item not found. Please enter a valid item name.")
# Calculate total price
total_price = 0
for item, quantity in cart:
    total_price += items[item] * quantity
if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount
    print(f"A discount of 10% has been applied: -${discount:.2f}")
print(f", the total price of your items is: ${total_price:.2f}")
