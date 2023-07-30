Yangyang Lian
07/10/2023
CS 10 Weekday number

1) Few test cases to understand the problem:
a) If January 1st is a Sunday (day 0 of the week) and we want to find the day of the week for the 14th day of the year, there have been 13 days that have passed since the start of the year. We add 0 (the day of the week for January 1st) and 13, which gives us 13. When we divide 13 by 7, we get a remainder of 6, so the 14th day of the year is a Saturday (day 6 of the week).
b) If January 1st is a Monday (day 1 of the week) and we want to find the day of the week for the 60th day of the year, there have been 59 days that have passed since the start of the year. We add 1 (the day of the week for January 1st) and 59, which gives us 60. When we divide 60 by 7, we get a remainder of 4, so the 60th day of the year is a Friday (day 4 of the week).
2) To solve this problem, we can follow these steps:
Determine the day of the week for January 1st of the year, represented as a value from 0 to 6, with 0 representing Sunday, 1 representing Monday, and so on.
Calculate the number of days that have passed since the start of the year up to the given day. This can be done by subtracting 1 from the day of the year.
Add the day of the week for January 1st to the number of days that have passed.
Calculate the remainder of this number when divided by 7.
The remainder will give us the day of the week for the given day of the year, represented as a value from 0 to 6, with 0 representing Sunday, 1 representing Monday, and so on.
  
def get_day_of_week(jan1_day, day_of_year):
  days_since_start_of_year = day_of_year - 1
  day_of_week = (jan1_day + days_since_start_of_year) % 7
  return day_of_week

jan1_day = int(input("Enter the day number in week of the first day of year: "))
day_of_year = int(input("Enter the day number of the year that you want to find out the day number in week: "))
day_of_week = get_day_of_week(jan1_day, day_of_year)
print(f"That will be day number: {day_of_week}")
