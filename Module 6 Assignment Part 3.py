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
datetime_object = datetime.now()
def heightandtime(x, y, z): 
    print("Height = ",x," feet and ",y," inches.") 
    print(z) 
x = input("Feet:") 
y = input("Inches:") 
heightandtime(x, y, datetime_object) 