# This is an email generator for universities in south africa. It takes the first and last name, and the name of the university of the user and generates an email address in the format: first.last@university.ac.za


firstName = input("Please enter your first name: ").split()
lastName = input("Please enter your last name: ").split()
university = input("Please enter the name of your university: ").split()

email = f"{firstName[0]}.{lastName[0]}1@{university[0]}.ac.za"

print(f"Your generated email address is: {email.lower()}")