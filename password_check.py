import string

special_chars = string.punctuation

password = input("Please enter a sufficient password: ")

has_length = len(password) >= 7
has_special = any(char in special_chars for char in password)
has_number = any(char.isdigit() for char in password)

if has_length and has_special and has_number:
    print("Password is valid")
else:
    print("\nPassword is not valid")
    if not has_length:
        print("\nPassword must be at least 7 characters long.")
    if not has_special:
        print("\nPassword must contain at least one special character.")
    if not has_number:
        print("\nPassword must contain at least one number.")
    print("Please try again")

