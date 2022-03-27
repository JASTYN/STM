import csv

with open("E:\\customers.csv",'r') as custfile:
rows=csv.reader(custfile,delimiter=',')
for r in rows:
print(r)