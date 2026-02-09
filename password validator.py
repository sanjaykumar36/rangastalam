# password validator
while True:

    user_password = input("enter ur password: ")

    valid_length = len(user_password) >= 8
    has_upper = False
    has_lower = False
    has_having_digit = False

    # checking each character
    for char in user_password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_having_digit = True

    # final check
    if valid_length and has_upper and has_lower and has_having_digit:
        print("The password you entered is valid")
        break
    else:
        print("Your password is not valid")

        if not valid_length:
            print("- must be 8 characters")

        if not has_upper:
            print("- must contain upper character")

        if not has_lower:
            print("- must contain lower character")

        if not has_having_digit:
            print("- must include digits")
