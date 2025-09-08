input_income = float(input("Enter your monthly income: "))
input_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = input_income - input_expenses

interest_rate = 0.05
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {annual_savings}")