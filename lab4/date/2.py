from datetime import datetime, date, timedelta
tday = date.today()
kun = timedelta(days = 1)
print(tday - kun) #Yesterday
print(tday) #Today
print(tday + kun) #Tommorow
