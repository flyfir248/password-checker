import re

def check_password_strength(password):
    if len(password) < 8:
        return "Too Short"
    elif re.search("[0-9]",password) is None:
        return "Weak"
    elif re.search("[a-z]",password) is None or re.search("[A-Z]",password) is None:
        return "Weak"
    elif re.search("[@#$]",password) is None:
        return "Weak"#
    else:
        return "Strong"

password = input("Enter your password: ")
print(check_password_strength(password))