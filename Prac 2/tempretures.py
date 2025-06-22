"""CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

# Constants
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """Function docstring"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_to_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit and print the result"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def convert_fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius and print the result"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

# Start the program
main()
