
def interest_calculator():
    # Months
    months = ["january", "february", "mars", "april", "mai", "june", "july", "august", "september", "october", "november", "december"]
    # Question to the user
    amount_borrowed = int(input("Please enter the amount borrowed: "))
    annual_interest_rate = int(input("Please enter the annual interest rate in percentage: "))
    amount_of_years = int(input("Please enter the amount of years: "))
    starting_month = input("Please enter the starting month: ")
    starting_year = int(input("Please enter the starting year: "))
    # Value initilizer
    annual_interest_rate = annual_interest_rate/100 + 1
    total_months_amount = amount_of_years * 12
    principal_monthly_amount = amount_borrowed / total_months_amount
    counter = 0
    # Check a valid month
    if ( not starting_month.lower() in months):
        print("You entered a wrong month")
        return
    # Detect month index
    month_index = months.index(starting_month.lower())
    flag = False
    while counter < total_months_amount:
        # Check if we started a new years depending on the starting month
        if (counter % 12 == 0 and flag):
            principal_monthly_amount *= annual_interest_rate
        # Format the output
        print_value = f'{months[month_index].capitalize():<10}/ {starting_year:}'
        print(f'{print_value:<15} = {principal_monthly_amount:.2f}')
        # Increment the month
        month_index += 1
        counter += 1
        # Check if we reached a new month depending on the starting month
        if (counter % 12 == 0):
            flag = True
        month_index %= 12
        if (month_index == 0):
            starting_year += 1
    
interest_calculator()
