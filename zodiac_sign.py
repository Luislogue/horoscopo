def zodiac_sign(month, day):
	sign = 'N/A'
	
	if month == 12:
		sign = 'Sagittarius' if (day < 22) else 'capricorn'
	elif month == 1:
		sign = 'Capricorn' if (day < 20) else 'aquarius'
	elif month == 2:
		sign = 'Aquarius' if (day < 19) else 'pisces'
	elif month == 3:
		sign = 'Pisces' if (day < 21) else 'aries'
	elif month == 4:
		sign = 'Aries' if (day < 20) else 'taurus'
	elif month == 5:
		sign = 'Taurus' if (day < 21) else 'gemini'
	elif month == 6:
		sign = 'Gemini' if (day < 21) else 'cancer'
	elif month == 7:
		sign = 'Cancer' if (day < 23) else 'leo'
	elif month == 8:
		sign = 'Leo' if (day < 23) else 'virgo'
	elif month == 9:
		sign = 'Virgo' if (day < 23) else 'libra'
	elif month == 10:
		sign = 'Libra' if (day < 23) else 'scorpio'
	elif month == 11:
		sign = 'Scorpio' if (day < 22) else 'sagittarius'
	print("Tu signo zodiacal es :",sign)
	return sign
