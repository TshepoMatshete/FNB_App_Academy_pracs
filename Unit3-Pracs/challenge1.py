kilometers = float(input("Please enter the number of kilometers you want to drive: "))
petrol_price = float(input("Please enter the current petrol price per liter (R): "))

liters_needed = kilometers / 10
total_cost = round(liters_needed * petrol_price, 2)

print(f"The total cost for your trip is: R{total_cost}")