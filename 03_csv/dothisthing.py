import csv, random


def occupationRandom():
    with open('occupations.csv', mode='r') as target:
        reader = csv.reader(target)
        next(reader)
        holddict = {}
        for row in reader:
            holddict[row[0]] = (float(row[1]))
    heavylist = []
    keys = []
    for i in holddict:
        if i != 'Total':
            heavylist.append(holddict[i])
            keys.append(i)

    return random.choices(keys, heavylist, k=1)
