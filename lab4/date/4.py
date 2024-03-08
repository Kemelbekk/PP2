from datetime import datetime
def san(fday,sday):
    dif = sday - fday
    sdif = dif.total_seconds()
    return sdif
date_format = "%Y-%m-%d %H:%M:%S"
date1_str = input()
date2_str = input()
date1 = datetime.strptime(date1_str,date_format)
date2 = datetime.strptime(date2_str,date_format)
a = san(date1,date2)
print(a)