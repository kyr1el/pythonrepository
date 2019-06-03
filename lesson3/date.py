from datetime import datetime, timedelta
dt_now = datetime.now()
delta = timedelta(days=1)
delta1 = timedelta(days=30)
yesterday = dt_now - delta
month_ago = dt_now - delta1
print(dt_now)
print(yesterday)
print(month_ago)

date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)