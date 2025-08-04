def check_password_strength(password):
    
    if len(password) < 8:
        return False

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False
    
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return False
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break
    if not has_special:
        return False
    
    return True

print("Password Requirements:")
print("- Atleast 8 characters")
print("- Atleast 1 uppercase letter")
print("- Atleast 1 lowercase letter") 
print("- Atleast 1 number")
print("- Atleas1 1 special character")
print()


password = input("Enter password: ")


if check_password_strength(password):
    print("This is a strong password!")
else:

    print("The password is weak, please try again!")
