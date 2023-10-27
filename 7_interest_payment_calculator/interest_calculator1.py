# P = a ÷ { [ (1 + r)^n ] - 1 } ÷ [ r (1 + r)^n]
# a:principal/r:monthly intrest rate(annual/12)/n: months number
# AMORTIZING LOAN CALCULATIONS MADE SIMPLE
#  the formula for a fixed-rate loan payment

def interest_calculator():
    principal = int(input("Please enter the loan amount: "))
    annual_interest = int(input("Please enter the annual interst: "))
    amount_of_years = int(input("Please enter the amout of years: "))
    
    number_of_months = amount_of_years * 12
    monthly_interest_rate = annual_interest / 1200
    monthly_payment =  (principal * monthly_interest_rate * ((1 + monthly_interest_rate)**number_of_months))/(((1 + monthly_interest_rate)**number_of_months) - 1)
    print(f'Mothly payment is {monthly_payment:.2f}')
interest_calculator()
