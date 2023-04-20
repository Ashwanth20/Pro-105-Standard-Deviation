import math
import csv
with open("data.csv", newline = "") as f :
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]
def formula(data):
    size = len(data)
    sum = 0
    for x in data:
        sum += int(x)
    mean = sum/size
    return mean

squaredlist = []
for number in data:
    a = int(number) - formula(data)
    a = a**2
    squaredlist.append(a)

total = 0
for i in squaredlist:
    total = total + i

result = total/(len(data) - 1)
stddeviation = math.sqrt(result)
print(stddeviation)
