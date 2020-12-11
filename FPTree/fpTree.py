import pandas as pd
import math


dataSet = pd.read_excel('FptreeDataset.xlsx')
allItem = dataSet.Item.values.tolist()

ItemList = list()
for i in allItem:
    for j in i:
        if j == ',' or j == ' ':
            pass
        else:
            ItemList.append(j)
df = pd.DataFrame(ItemList)
firstColumn = df[0]
print('##########Step 1###########')
print('Ele freq')
print(firstColumn.value_counts(sort=False))

print('Calculation of support value if available other wise enter 0')
percent = float(input('Enter percentage:'))
frequencyList =  firstColumn.value_counts(sort=False).tolist()
maxvalue = max(frequencyList)

print((percent/100.00) * maxvalue)
thresholdValue = round((percent/100.00) * maxvalue)
print(thresholdValue)



df2 = pd.DataFrame(firstColumn.value_counts(sort=True))
print('\n##########Step 2###########')
print('Frequency of Occurrence')
print(df2)



