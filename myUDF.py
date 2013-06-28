#/usr/bin/jython

from datetime import datetime

@outputSchema("day:chararray")
def day(date):
  return date.split(" ")[0];

@outputSchema("yes:boolean")
def greaterthanday(day1, day2):
  date1 = datetime.strptime(day(day1), '%Y-%m-%d');
  date2 = datetime.strptime(day2, '%Y-%m-%d');
  return date1 > date2;

  
@outputSchema("yes:chararray")
def mininumDate(days):
	string2 = "9999-12-13"
	minDate = datetime.strptime('9999-12-31', '%Y-%m-%d');
	for item in days:
		string2 = str(item)[3:-3]
		date = datetime.strptime(string2, '%Y-%m-%d');
		if (date < minDate):
			minDate = date;
	return str(minDate);


@outputSchema("yes:chararray")
def week(date):
	d = datetime.strptime(date, '%Y-%m-%d');
	i = d.isocalendar();
 	s = str(i[0]) + "-" +str(i[1]);
	return s;


@outputSchema("yes:boolean")
def isSameMonth(date1, date2):
	d1 = datetime.strptime(date1, '%Y-%m-%d');
	d2 = datetime.strptime(date2, '%Y-%m-%d');
	return d1.year == d2.year and d1.month == d2.month;

