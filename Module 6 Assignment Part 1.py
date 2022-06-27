#Attempting Problem Number 1. 
#for line in sys.stdin: 
#    data = line.strip().split("\t") 
#    if len(data) == 6: 
#        data, time, store, item, cost, payment = data 
#        print ("{0}\t{1}".format(item, cost))
# Added parentheses to the "print" function. The code still does not print 
# anything in the terminal. 

#Solution provided by Dr. Friedman
import sys 
from datetime import datetime
from datetime import time
from datetime import date

def main():

    dt = datetime.now()
   #utc = datetime.utcnow()
    time_string = dt.strftime("%X")

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            _date, _time, store, item, cost, payment = data
            print ("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")
main()