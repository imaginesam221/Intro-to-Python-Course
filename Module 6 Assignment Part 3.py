from datetime import datetime 
from datetime import timedelta 

#Example Code given: 
d = timedelta(microseconds=-1) 
print(d.days, d.seconds, d.microseconds) 

#Problem 
#Converting time blocks into minutes. 100 days = 144,000 min.; 
# 10 hours = 600 min.; + 13 min. 
# Which was equal to 144,613 total minutes. 

broken_clock = timedelta(minutes=144613) 
print(broken_clock.days, broken_clock.seconds)  

#Problem 4
datetime_addition = datetime.now()
def height_and_time_variables(x, y, z): 
    print("Height = ",x," feet and ",y," inches at ",datetime_addition,"") 
x = input("Feet:") 
y = input("Inches:") 
height_and_time_variables(x, y, datetime_addition) 
