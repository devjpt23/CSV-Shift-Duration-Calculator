import csv
from datetime import datetime

def calculatingDuration(start,end):
    timeFormat = '%H:%M'
    startTime = datetime.strptime(start,timeFormat)
    endTime = datetime.strptime(end,timeFormat)
    duration = endTime - startTime
    return str(duration)

with open("this.csv") as file:
    fileReader = csv.reader(file)
    fileData = list(fileReader)

# EmpID,EmpName,StartTime,EndTime
newColumn = fileData[0]
newColumn = ['EmpID','EmpName','StartTime','EndTime','ShiftTime']
fileData[0] = newColumn

for row in fileData[1:]:
    startTime = row[2]
    endTime = row[3]
    shiftTime = calculatingDuration(startTime,endTime)
    row.append(shiftTime)

with open("thisReal.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(fileData)

print("Changes have been made sucessfully. (New column and column data has been added!)")
