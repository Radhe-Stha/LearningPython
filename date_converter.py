"""# importing
>>> import datetime
>>> import datetime_nepali

# today's date
>>> datetime.date.today()
>>> datetime_nepali.date.today()

# now datetime
>>> datetime.datetime.now()
>>> datetime_nepali.datetime.now()

# creating date object
>>> datetime.date(2020, 9, 4)
>>> datetime_nepali.date(2077, 5, 19)

# creating datetime object
>>> datetime.datetime(2020, 9, 4, 8, 26, 10, 123456)
>>> datetime_nepali.datetime(2077, 5, 19, 8, 26, 10, 123456)

# date/datetime formatting
>>> datetime_nepali.datetime(2077, 5, 19, 8, 26, 10, 123456).strftime("%d %B %Y")
# 19 Bhadau 2077

# datetime parsed from string (strptime)
>>> datetime_nepali.datetime.strptime('2077-09-12', '%Y-%m-%d')
# datetime_nepali.datetime(2077, 9, 12, 0, 0)

# date/datetime formatting with Nepali unicode support
>>> datetime_nepali.date(1977, 10, 25).strftime('%K-%n-%D (%k %N %G)')
# १९७७-१०-२५ (७७ माघ आइतबार)

# datetime.timedelta addition/subtraction
>>> datetime_nepali.date(1990, 5, 10) + datetime.timedelta(days=350)
# datetime_nepali.date(1991, 4, 26)
>>> datetime_nepali.datetime(1990, 5, 10, 5, 10, 20) + datetime.timedelta(hours=3, minutes=15)
# datetime_nepali.date(1990, 5, 10, 8, 25, 20)

# convert B.S to A.D date and vice-versa
>>> datetime_nepali.date(1999, 7, 25).to_datetime_date()
# datetime.date(1942, 11, 10)
>>> datetime_nepali.date.from_datetime_date(datetime.date(1942, 11, 10))
# datetime_nepali.date(1999, 7, 25)

# Bikram Sambat monthly calendar
>>> datetime_nepali.date(2078, 1, 1).calendar()

          Baishakh 2078
Sun  Mon  Tue  Wed  Thu  Fri  Sat
                1    2    3    4
5     6    7    8    9   10   11
12   13   14   15   16   17   18
19   20   21   22   23   24   25
26   27   28   29   30   31"""