import shared_function as sf

#   To get current date in short you should call
print("function - get_current_date")
data = sf.get_current_date()
print(type(data))
print(data)

#   To get current date time you should call
print("function - get_current_date_time")
data = sf.get_current_date_time()
print(type(data))
print(data)

#   To get current date/time in custom format, you should call
#   Current date without year and day of week
print("function - get_current_date_time_custom_format")
date_time_format = "%m %d, %A"
data = sf.get_current_date_time_custom_format(date_time_custom_format=date_time_format)
print(type(data))
print(data)

#   To get tomorrow or yesterday you should call
print("function - get_tomorrow")
data = sf.get_tomorrow()
print(data)
print(type(data))
print("function - get_yesterday")
data = sf.get_yesterday()
print(type(data))
print(data)

#   To get next date after several days (+2 days)
print("function - get_date_period +2 days")
cur_date = sf.get_current_date()
data = sf.get_date_period(current_date=cur_date, period=2)
print(type(data))
print(str(cur_date) + " +2 days = " + str(data))

#   To get previous date before several days (-3 days) in custom format (month, day)
print("function - get_date_period - 3 days")
cur_date = sf.get_current_date()
data = sf.get_date_period(current_date=cur_date, period=-3)
print(type(data))
print(str(cur_date) + " -3 days = " + str(data))

#   To get next month
print("function - get_month_next")
data = sf.get_month_next(sf.get_current_date())
print(type(data))
print(data)

#   To get previous month
print("function - get_month_previous")
data = sf.get_month_previous(sf.get_current_date())
print(type(data))
print(data)

#   To get next month after current date (+3 months)
print("function - get_month_period +3 month")
data = sf.get_month_period(sf.get_current_date(), period=3)
print(type(data))
print(data)

#   To get previous month before current date (-6 months)
print("function - get_month_period -6 month")
data = sf.get_month_period(sf.get_current_date(), period=-6)
print(type(data))
print(data)

#   Get number of days in month
print("function - get_days_number")
data = sf.get_days_number(sf.get_current_date())
print(type(data))
print(data)

#   If you want get first day of current month you can call
print("function - get_first_day_of_month")
data = sf.get_first_day_of_month(sf.get_current_date())
print(type(data))
print(data)

#   For get first day of next month you can call
print("function - get_first_day_of_next_month")
data = sf.get_first_day_of_next_month(sf.get_current_date())
print(type(data))
print(data)

#   For get first day of previous month you can call
print("function - get_first_day_of_previous_month")
data = sf.get_first_day_of_previous_month(sf.get_current_date())
print(type(data))
print(data)

#   Get last day of month
print("function - get_last_day_of_month")
data = sf.get_last_day_of_month(sf.get_current_date())
print(type(data))
print(data)

#   Get last day of next month
print("function - get_last_day_of_next_month")
data = sf.get_last_day_of_next_month(sf.get_current_date())
print(type(data))
print(data)

#   Get last day of previous month
print("function - get_last_day_of_previous_month")
data = sf.get_last_day_of_previous_month(sf.get_current_date())
print(type(data))
print(data)
