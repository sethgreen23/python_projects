

def leap_year_checker():
    print("------Leap Year Checker------")
    year = int(input("Please enter the year you want to check: "))
    is_leap_year = (year % 4 == 0 and  year % 100 != 0) or year % 400 == 0
    if is_leap_year:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not a leap year.")
def check_user_input():
    user_input = input("Do you want to check another year? (y/n): ")
    while not user_input.lower() in'yn':
        user_input = input("Please choose between y/n: ")
        if user_input == 'n':
            return -1
    if user_input.lower() == 'n':
        return -1
    return 1

while True:
    leap_year_checker()
    if (check_user_input() == -1):
        break
