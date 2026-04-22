'''Custom Password Validator

Rules:

Min 8 chars
At least 1 uppercase, 1 lowercase, 1 digit
Use:
string operations
loops + conditionals
Raise custom exception if invalid'''
class PasswordValidationError(Exception):
    # Custom exception for password validation errors
    pass
def validate_password(password):
    # Check if the password meets the minimum length requirement
    if len(password) < 8:
        raise PasswordValidationError("Password must be at least 8 characters long.")
    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    if not (has_upper and has_lower and has_digit):
        raise PasswordValidationError("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
    return True
# Example usage
try:
    user_password = input("Enter a password to validate: ")
    if validate_password(user_password):
        print("Password is valid.")
except PasswordValidationError as e:
    print(f"Password validation error: {e}")
