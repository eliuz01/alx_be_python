income = int(input("Enter your monthly income: "))
expenses =int(input("Enter your total monthly expenses: "))

savings = income - expenses 
projected_Savings = (savings * 12) + (savings * 12 * 0.05)
print(f"Your monthly savings are ${savings}")
print(f"projected savings after one year, with interest, is: ${projected_Savings}.")