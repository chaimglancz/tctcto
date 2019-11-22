import time
from datetime import datetime
def IsYearLeap(year):#Lab_3_3_1(1)
    if year%4!=0:
        return False
    elif year%400==0:
        return True
    elif year%100==0:
        return False
    else:
        return True
    
def DaysInMonth(year,month):#Lab_3_3_1(2)
    if month==1 or month==3 or month==5 or month==7 \
       or month==8 or month==10 or month==12:
        return 31
    elif month==4 or month==6 or month==9 or month==11:
        return 30
    elif IsYearLeap(year)==True and month==2:
        return 29
    elif IsYearLeap(year)==False and month==2:
        return 28
    else:
        return None

def put_zero(num):
    if len (str(num)) < 2:
        return '0'+str(num)
    else:
        return str(num)
def disply(tm):
    hour=int((tm%86400)//3600)
    minute=int((tm%3600)//60)
    second=int(tm%60)
    day = int(tm//86400)
    day += 1
    year = 1970
    while True:
        if not IsYearLeap(year) :
            if day > 365 :
                day -= 365
                year += 1
            else:
                break
        if IsYearLeap(year) :
            if day > 366 :
                day -= 366
                year += 1
            else:
                break
    mon = 1        
    while True:
        if day > DaysInMonth(year,mon) :
            day -= DaysInMonth(year, mon)
            mon += 1
        else:
            year = put_zero(year)
            mon = put_zero(mon)
            day = put_zero(day)
            hour = put_zero(hour)
            minute = put_zero(minute)
            second = put_zero(second)
            total=year + '-' + mon + '-' + day + ' ' + hour + ':' + minute + ':' + second
            return total
finel=disply(time.time()-14400)
print(finel)
print(str(datetime.now())[0:19])
