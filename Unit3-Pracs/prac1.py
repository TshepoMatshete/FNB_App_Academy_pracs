# Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.

# **Requirements**

# ~ Use float(input()) to collect two numbers from the user
# ~ Calculate and display: addition, subtraction, multiplication, division
# ~ Calculate and display: floor division (//) and modulus (%)
# ~ Round all results to 2 decimal places using round()
# ~ Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
# ~ Display all results in a formatted table using f-strings

num1 = float(input("please enter a number here: "))
num2 = float(input("please enter another number here: "))

addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)
#added an extra step to handle division by zero in the arithmetic operations below
division = round(num1 / num2, 2) if num2 != 0 else "Error: Division by zero is not allowed."
floor_division = round(num1 // num2, 2) if num2 != 0 else "Error: Division by zero is not allowed."
modulus = round(num1 % num2, 2) if num2 != 0 else "Error: Division by zero is not allowed."

print(f"{'Operation':<20}{'Result':<20}")
print(f"{'Addition':<20}{addition:<20}")
print(f"{'Subtraction':<20}{subtraction:<20}")
print(f"{'Multiplication':<20}{multiplication:<20}")
print(f"{'Division':<20}{division:<20}")
print(f"{'Floor Division':<20}{floor_division:<20}")
print(f"{'Modulus':<20}{modulus:<20}")