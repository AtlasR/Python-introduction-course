interest_rate_input = float(input("Please enter the interest rate as a whole number e.g., 8 for 8%): "))
initial_investment =float(input("Please enter the initial investment amount (please note the initial investment should be entered as a whole number): "))

interest_rate = interest_rate_input / 100
current_balance = initial_investment
target_balance = initial_investment * 2
years = 0

while current_balance < target_balance:
    current_balance += current_balance * interest_rate
    years += 1

    message = (f'It will take {years} years for your investment of ${initial_investment:,.2f} 'f"to double to {current_balance:,.2f}")
    print(message)