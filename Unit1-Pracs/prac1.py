firstName = input("enter your first name here: ")
surname = input("enter your surname here: ")
age = int(input("please enter your age here: "))
favourite_number = float(input("please enter your favourite number here: "))

print(f"Welcome, {firstName} {surname}!")
print(f" Here is your name in UPPER cae {firstName.upper()} {surname.upper()} \n Here is your name in Tittle case {firstName.title()} {surname.title()}")

print(f"Your age in months is: {age * 12} months")
print(f"Your favourite number is: {round(favourite_number, 2)}")

print(f"The data types for all the variables is as follows: \n firstName: {type(firstName)} \n surname: {type(surname)} \n age: {type(age)} \n favourite_number: {type(favourite_number)}")