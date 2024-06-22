import csv
from datetime import datetime

def calculatingDuration(start,end):
    timeFormat = '%H:%M'
    startTime = datetime.strptime(start,timeFormat)
    endTime = datetime.strptime(end,timeFormat)
    duration = endTime - startTime
    return str(duration)

with open("this.csv","r") as file:
    reader = csv.reader(file)
    data = list(reader)

newColumn = data[0]
newColumn = ['EmpName', 'StartTime', 'EndTIme','ShiftDuration']
data[0] = newColumn

for row in data[1:]:
    startTime = row[1]
    endTime = row[2]
    shiftTime = calculatingDuration(startTime,endTime)
    row.append(shiftTime)

with open("newFile.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("New column and its data has been added successfully! ")
