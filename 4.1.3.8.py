def is_Year_Leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_In_Month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_Year_Leap(year):
		res = 29
	return res

def day_Of_Year(year, month, day):
	days = 0
	for m in range(1, month):
		md = days_In_Month(year, m)
		if md == None:
			return None
		days += md
	md = days_In_Month(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(day_Of_Year(2001, 11, 30))
