import pandas as pd
import math

########### Functional Part ############
def customround(M):
    n = M - .50
    if n % 2 == 0:
        M = math.ceil(M)
    else:
        M = round(M)
    return float(M)
########### Functional Part ############

print('##########Step 1###########')
dataSet = pd.read_excel('FptreeDataset.xlsx')
allItem = dataSet.Item.values.tolist()

combItem = dataSet.Item.values
combTid = dataSet.TID.values
TidItemDict= dict()
for i in range(len(combItem)):
    TidItemDict[combTid[i]] = [x for x in combItem[i] if x != ',' if x!=' ']


ItemList = list()
for i in allItem:
    for j in i:
        if j == ',' or j == ' ':
            pass
        else:
            ItemList.append(j)
df = pd.DataFrame(ItemList)
firstColumn = df[0]
# print('first',firstColumn)

print(ItemList)
print('Ele freq')
print(firstColumn.value_counts(sort=False))

print('\n##########Step 2###########')

print('Sorted DataSet')
df2 = pd.DataFrame(firstColumn.value_counts(sort=True, dropna=True))
print(df2)

print('\n##########Step 3###########')
print('Enter support value if available, otherwise enter 0')
percent = float(input('Enter percentage:\n'))
frequencyList =  firstColumn.value_counts(sort=False).tolist()

maxvalue = max(frequencyList)
passAble = (percent/100.00) * len(dataSet)

thresholdValue = customround(passAble) #######thresholdValue############
print('Threshold value: ',thresholdValue,'\n')
df3 = df2.reset_index()
df3.columns = ['Elements', 'Frequency']
dropIndex = df3[df3['Frequency'] < thresholdValue].index.values
df3 = df3.drop(dropIndex)
############ need to be changeable threshold condition ###
print('Frequency of Occurrence')
print(df3)

print('\n##########Step 4###########')
print(TidItemDict)
orderedItem = df3['Elements'].values.tolist()
print('Ordered Item: ',orderedItem)
lastDict = dict()
for key,value in TidItemDict.items():
    lastDict[key] = list() #is a awesome logic
    for i in orderedItem:
        if i in value:
            lastDict[key].append(i)
print('\nFinal DataSet: ',lastDict)








