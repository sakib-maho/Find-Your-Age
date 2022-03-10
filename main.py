from datetime import date


def Calculate_My_Age(input_day, input_month, input_year):
    today = date.today()

    day, month, year = today.strftime("%d"), today.strftime("%m"), today.strftime("%Y")

    my_age_years = int(year) - input_year
    my_age_month = int(month) - input_month
    my_age_month = my_age_month * -1 if my_age_month < 0 else my_age_month
    my_age_day = int(day) - input_day
    my_age_day = my_age_day * -1 if my_age_day < 0 else my_age_day
    print(f"You're {my_age_years} Year(s), {my_age_month} Month(s), {my_age_day} Day(s) old...!!!")


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
