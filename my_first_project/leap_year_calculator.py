days_month = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 2020

if year % 4 == 0 and year % 100 != 0:
    days_month[1]=29

print(days_month[1])