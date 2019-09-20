import csv, random

with open('occupations.csv', mode='r') as target:
    reader = csv.reader(target)
    next(reader)
    holddict = {}
    for row in reader:
        holddict[row[0]] = (float(row[1]))
heavylist = []
keys = []
for i in holddict:
    if(i != 'Total'):
        heavylist.append(holddict[i])
        keys.append(i)
    #    while(holdnum > 0):
    #         heavylist.append(i)
    #         holdnum -= 1




print(random.choices(keys, heavylist, k=1))
print(holddict)
