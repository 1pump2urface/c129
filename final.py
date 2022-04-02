import csv
from email import header
dataset1 = []
dataset2 = []
with open("C:/Users/Administrator/Desktop/Python 2/classes/c129/final.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("C:/Users/Administrator/Desktop/Python 2/classes/c129/dataset_2_sorted.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1 = dataset1[0]
planetdata1 = dataset1[1:]
header2 = dataset2[0]
planetdata2 = dataset2[1:]
headers = headers1 + header2
planetdata = []
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("final1.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)