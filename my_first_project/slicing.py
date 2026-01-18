days_month = [31,28,31,30,31,30,31,31,30,31,30,31]

summer = days_month[5:8] #June to August : 6 to 8
first = days_month[:3] #Start at the beginning until index less than 3
last = days_month[-3:] #Start at the third to end element until the end

first_last = first + last

print(first_last)