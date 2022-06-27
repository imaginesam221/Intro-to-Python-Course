from datetime import datetime 
from datetime import timedelta 

#Problem Number 2, having to make functions for times and dates 
# with Python. 
#Starting with having the current date and time before adding or 
# subtracting time as per the problem recommendation. 

curr_datetime = datetime.now() 
curr_date = curr_datetime.date() 
curr_time = curr_datetime.time() 
print(curr_datetime) 

#Adjusting the date and time per instructions. 
date_time = datetime.now() 
time_diff = timedelta(
#Since we need to use days as a function, 365 days multiplied by 2 for 
# years yields 730 days not accounting for any leap years. 
                    days=730, 
                    seconds=-60 
) 
req_date_time = date_time + time_diff 
print(req_date_time) 