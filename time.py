import datetime

hour = datetime.datetime.now().hour
next_day = 24-hour

day = datetime.datetime.now().day + 1
days_left = 14 - day
hours = days_left*24 + next_day

print(hours)
