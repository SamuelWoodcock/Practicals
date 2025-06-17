"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

try:
    sales = float(input("Enter sales: $"))
    if 0>= sales:
        print("Error: Sales cannot be negative")
    elif sales >= 1000:
        bonus = .15 * sales
        print("Your bonus is,$",bonus)
    else:
        bonus = .10 * sales
        print("Your bonus is,$", bonus)
except ValueError:
    print("Error: please input a valid number")
