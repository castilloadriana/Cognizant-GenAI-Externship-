password = input("Enter a password: ")

upper= False
lower= False
digit= False
special= False

special_chars = "@#$"

for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    elif char in special_chars:
        special = True

missing = []

if len(password) < 8:
    missing.append("at least 8 characters")
if not upper:
    missing.append("one uppercase letter")
if not lower:
    missing.append("one lowercase letter")
if not digit:
    missing.append("one digit")
if not special:
    missing.append("one special character")

if not missing:
    print("Your password is strong! 💪")
else:
    print("Your password needs " + ", ".join(missing) + ".")

        




