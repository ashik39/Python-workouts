from datetime import datetime
current_date = datetime.now()
oneday_before = datetime.now() + timedelta(months=2)
print(current_date.strftime("%b"))
