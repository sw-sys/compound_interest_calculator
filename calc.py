# calculate the interest

def calcInterest(principal, interest, time_period, frequency):
    amount = principal * (1 + (interest / compounding_frequency)) ** (compounding_frequency * time_period)
    interest_amount = amount - principal
    return interest_amount

# get user input
principal = float(input("Enter the deposit amount: "))
interest = float(input("Enter the interest rate: "))
time_period = float(input("Enter the time period: "))
compounding_frequency = float(input("Enter the compounding frequency in years: "))

# print out
total_interest = calcInterest(principal, interest, time_period, compounding_frequency)
total_interest = round(total_interest, 2)

print(f"Total interest accrued is: £ {total_interest}")