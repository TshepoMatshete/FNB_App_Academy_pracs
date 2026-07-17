password = input("Please enter your secret password: ").strip().upper()
print(f"Your password hint: It starts with {password[0]} and ends with {password[-1]}")