#Program to convert user given AD date to BS date

import datetime
import datetime_nepali

eng_year = int(input("Enter English Year : "))
eng_month = int(input("Enter English Month : "))
eng_day = int(input("Enter English Day : "))

converter = datetime_nepali.date.from_datetime_date(datetime.date(eng_year, eng_month, eng_day))
print(f"Nepali date is : {converter}")