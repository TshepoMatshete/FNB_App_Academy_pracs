balance = 500
withdrawal_amount = float(input("Please enter the amount you want to withdraw: "))

if withdrawal_amount <= balance and withdrawal_amount > 0:
    balance -= withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")
elif withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")
else:
    print("Declined. Insufficient funds.")