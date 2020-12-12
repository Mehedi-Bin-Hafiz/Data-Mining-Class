from itertools import combinations
from operator import itemgetter
import pandas as pd

itemList = [
    ['1', '3', '4'],
    ['2', '3', '5'],
    ['1', '2', '3', '5'],
    ['2', '5'],
]
tempItem = []
itemNums = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
}

thVal = 2
for x in itemList:
    for y in x:
        itemNums[str(y)] += 1
        if y in tempItem:
            continue
        tempItem.append(y)
# print([x for x in itemNums])
# print(itemNums)
totalItemNumber = len(tempItem)

print('total item number  :       ', totalItemNumber)
print()
print()
# ========================set N
# totalItemNumber = 5
print('item counts :')
tempDic = itemNums.copy()

for x, y in itemNums.items():
    print(x, ' : ',  y)
    if y < thVal:
        del tempDic[x]

print('After removing values under threshold')
[print(x, ' : ', tempDic[x]) for x in tempDic]
print()
print()




print('set with 2 elements')
itemListSet2items = [*combinations(tempDic.keys(), 2)]
print(itemListSet2items)
print()
print()

itemNums = {}
print('two item set count')
for x, y in itemListSet2items:
    for z in itemList:
        if x in z and y in z:
            # print(x, y)
            itemNums['{},{}'.format(x, y)] = itemNums['{},{}'.format(x, y)]+1 if '{},{}'.format(x, y) in itemNums else 1

# print(itemNums)

tempDic = itemNums.copy()

for x, y in itemNums.items():
    print(x, ' : ', y)
    if y < thVal:
        del tempDic[x]

print('After removing values under threshold')
[print(x, ' : ', tempDic[x]) for x in tempDic]
print()
print()
print()


itemsIn2set = []
for x in tempDic.keys():
    keys = x.split(',')
    for y in keys:
        if y in itemsIn2set:
            continue
        itemsIn2set.append(y)
# print(itemsIn2set)

# itemListSet2items = [*combinations(itemsIn2set, 3)]
# print(itemListSet2items)
print()
print()







print('set with 3 elements')
itemListSet2items = [*combinations(itemsIn2set, 3)]
print(itemListSet2items)
print()
print()

itemNums = {}
print('three item set count')
for x, y, z in itemListSet2items:
    for k in itemList:
        if x in k and y in k and z in k:
            # print(x, y)
            itemNums['{},{},{}'.format(x, y, z)] = itemNums['{},{},{}'.format(x, y, z)]+1 if '{},{},{}'.format(x, y, z) in itemNums else 1

# print(itemNums)

tempDic = itemNums.copy()

for x, y in itemNums.items():
    print(x, ' : ', y)
    if y < thVal:
        del tempDic[x]

print('After removing values under threshold')
[print(x, ' : ', tempDic[x]) for x in tempDic]
print()
print()
print()


itemsIn2set = []
for x in tempDic.keys():
    keys = x.split(',')
    for y in keys:
        if y in itemsIn2set:
            continue
        itemsIn2set.append(y)
print(itemsIn2set)

itemListSet2items = [*combinations(itemsIn2set, 3)]
print(itemListSet2items)
print()
print()







