

def leap_year_checker():
    print("------Leap Year Checker------")
    year = int(input("Please enter the year you want to check: "))
    is_leap_year = (year % 4 == 0 and  year % 100 != 0) or year % 400 == 0
    if is_leap_year:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not a leap year.")
while True:
    leap_year_checker()
    user_input = input("Do you want to check another year? (y/n): ")
    while not user_input.lower() in'yn':
        user_input = input("Please choose between y/n: ")
        if user_input == 'n':
            break
    if user_input.lower() == 'n':
     break
