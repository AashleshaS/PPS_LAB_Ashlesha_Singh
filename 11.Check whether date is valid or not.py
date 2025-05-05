#List of days in each month(non leap year)
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]

#taking user input
year=int(input("year: "))
month=int(input("month: "))
day=int(input("day: "))

#check if it's a leap year
if(year%4==0 and year %100!=0)or(year%400==0):
	days_in_month[1]=29 # february has 29 days in a leap year

#validate the input date
if 1<=month<=12 and 1<=day<=days_in_month[month-1]:
	print("valid")

	#increment day
	day+=1

	#check if day exceeds the month's limit
	if day>days_in_month[month-1]:
		day=1 # reset day to 1
		month+=1 # move to next month

		if month>=12: #if mont wxceeds 12,go to next year
			month=1
			year+=1
	print(f"incremented date: {year}-{month:02d}-{day:02d}")
else:
	print("invalid")