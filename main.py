from datetime import date


def Calculate_My_Age(input_day, input_month, input_year):
    today = date.today()

    day, month, year = today.strftime("%d"), today.strftime("%m"), today.strftime("%Y")
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if input_day > int(day):
        month = int(month) - 1
        day = int(day) + days_in_month[input_month - 1]

    if input_month > int(month):
        year = int(year) - 1
        month = int(month) + 12

    calculated_date = int(day) - input_day
    calculated_month = month - input_month
    calculated_year = year - input_year

    print(f"You're {calculated_year} Year(s), {calculated_month} Month(s), {calculated_date} Day(s) old...!!!")


input_day, input_month, input_year = map(int, input(
        'Enter your Birthdate in the following format: DD MM YYYY: ').split())

months_with_30_days = [4, 6, 9, 11]
months_with_31_days = [1, 3, 5,  7, 8,  10,  12]

valid_data = False

if 0 < input_day <= 31 and 0 < input_month <= 12 and input_year > 0:
    if input_month in months_with_31_days and input_day <= 30:
        valid_data = True
    elif input_month == 2 and input_day <= 28:
        valid_data = True
    elif input_month in months_with_31_days:
        valid_data = True
    else:
        pass
else:
    pass


if valid_data:
    Calculate_My_Age(input_day, input_month, input_year)
else:
    print('Invalid Input...!!!')
