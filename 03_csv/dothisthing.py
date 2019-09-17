import csv, random

with open('occupations.csv', mode='r') as target:
    reader = csv.reader(target)
    next(reader)
    holddict = {}
    for row in reader:
        holddict[row[0]] = (float(row[1]) * 10)
heavylist = []
for i in holddict:
    if(i != 'Total'):
        holdnum = (holddict[i])
        while(holdnum > 0):
            heavylist.append(i)
            holdnum -= 1



print(len(heavylist))
print(random.choice(heavylist))
print(holddict)
