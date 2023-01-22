import csv
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Current Time =", current_time)

# get current time and also date



def writeline():
    with open('lines.csv','w') as file:
        f_csv = csv.writer(file)
        l = ['a','b','c']
        l.append(current_time)
        print(l)
        f_csv.writerow(l)



writeline()
