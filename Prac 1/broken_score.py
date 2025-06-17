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
