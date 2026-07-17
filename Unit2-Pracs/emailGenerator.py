# This is an email generator for universities in south africa. It takes the first and last name, and the name of the university of the user and generates an email address in the format: first.last@university.ac.za


firstName = input("Please enter your first name: ").strip()
lastName = input("Please enter your last name: ").strip()
university = input("Please enter the name of your university: ").strip()

email = f"{firstName}.{lastName}1@{university}.ac.za"

print(f"Your generated email address is: {email.lower()}")