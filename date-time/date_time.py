import datetime

now = datetime.datetime.now()
print(f"Current date is {now}")
today_date = datetime.date.today()
print(f"Today is : {today_date}")

#save date
save_date = datetime.date(1997,5,15)
print(save_date)

#change date format
current_date = datetime.date.today()
print(current_date.strftime("%y/%m/%d"))

