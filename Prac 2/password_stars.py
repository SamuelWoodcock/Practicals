"""Program asks user for a password, that has more than 8 characters"""
from _ast import While

minimum_length = 8

def get_password():
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long, Please Try Again")
        password = input("Enter password: ")
    return password

def main():
    password = get_password()
    print("*" * len(password))

main()