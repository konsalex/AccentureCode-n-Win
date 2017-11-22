from datetime import datetime, timedelta
import holidayapi

hapi = holidayapi.v1('11b227ec-f5ad-492e-b6a2-0588308b0c6c')

parameters = {
	# Required
	'country': 'GR',
	'year':    2017,
	# Optional
	# 'month':    7,
	# 'day':      4,
	# 'previous': True,
	# 'upcoming': True,
	# 'public':   True,
	# 'pretty':   True,
}

holidays = hapi.holidays(parameters)

startingDate1 = '24/11/2017'
startingDate2 = '24/11/2017'

endingDate1 = '30/01/2018'
endingDate2 = '15/12/2017'

#days = np.busday_count(date1, date2)

ed = 45

sdate1 = datetime.strptime(startingDate1, "%d/%m/%Y").date()
sdate2 = datetime.strptime(startingDate2, "%d/%m/%Y").date()

date1 = datetime.strptime(startingDate1, "%d/%m/%Y").date()
date2 = datetime.strptime(startingDate2, "%d/%m/%Y").date()

endingDate1 = datetime.strptime(endingDate1, "%d/%m/%Y").date()
endingDate2 = datetime.strptime(endingDate2, "%d/%m/%Y").date()

if (date2 < date1):
	currentdate = date2
else:
	currentdate = date1

print('The day one starts working:')
print(currentdate)

counter = 0;

if (date1 < endingDate1 and date1 >= sdate1):
	date1 += timedelta(days=1)
	counter += 1

if (date2 < endingDate2 and date2 >= sdate2):
	date2 += timedelta(days=1)
	counter += 1


while (counter<ed):
	currentdate += timedelta(days=1)

	if (currentdate.weekday() >= 5):
		currentdate += timedelta(days=1)
		continue

	if (currentdate in holidays):
		currentdate += timedelta(days=1)
		continue

	if (date1 < endingDate1 and date1 >= sdate1):
		date1 += timedelta(days=1)
		counter += 1

	if (date2 < endingDate2 and date2 >= sdate2):
		date2 += timedelta(days=1)
		counter += 1
	#currentdate += timedelta(days=1)


print('Estimation Date')
print(currentdate)
