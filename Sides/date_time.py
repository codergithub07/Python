from datetime import date
import time

# 1) today = date(2022, 11, 5) # Setting a date ; Requires "from datetime import date"
#    today = date.today() # Getting today's date ; Requires "from datetime import date"
#    print("Today date is: ", today)

# 2) today = date.today() # Requires "from datetime import date"
#    print("Current Year: ", today.year)
#    print("Current Month: ", today.month)
#    print("Current Day: ", today.day)

# 3) date_time = datetime.fromtimestamp(1672531200) # Time passed in seconds after 01-01-1970 05:30 AM
#    print("Date_Time from timestamp: ", date_time)

# 4) today = date.today()
#    str = date.isoformat(today) # Converts date into string type
#    print("String Format is: ", str)
#    print(type(str))

# 5) print("", time.ctime()) # Gives 'Day, Month, Date, Time(in 24 hrs), Year' in string class NOTE :- Requires time module

# 6) a = time.localtime() # Sets local time to a variable
#    c = time.asctime(a) # Gives 'Day, Month, Date, Time(in 24 hrs), Year' in string class NOTE :- Requires time module
#    print(c)