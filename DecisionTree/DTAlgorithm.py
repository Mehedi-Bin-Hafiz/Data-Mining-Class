import pandas as pd
import tabula
import math


dataSet = pd.read_excel('examdata.xlsx')


print('\n#################Entropy Part#####################\n')

############ look me #############
dtClass = dataSet.play ##must assign decision class
############# look me ############



dtClassCountedValue = dtClass.value_counts(sort=True).tolist()
maxDtClassElementLen = len(dtClassCountedValue)
sumOfCountedValue = sum(dtClassCountedValue)

dtClassEntropy = 0
for i in dtClassCountedValue:
    print('-({0}/{1})*log2({0}/{1})'.format(i,sumOfCountedValue),end='')
    dtClassEntropy += -(i/sumOfCountedValue)*math.log2((i/sumOfCountedValue))

print('= {:.2f}'.format(dtClassEntropy))

###calculation of entropy of each attribute###

allHeader = list(dataSet.columns.values)
print('All headers: ', allHeader)


###################Header modification area#########################

allHeader.pop(0)  ### it removes 0 number column
dependent = allHeader.pop()
print('Independent attributes: ', allHeader, end='\n')

###################Header modification area#########################


entropyLis = list()
entropyDict = dict()

for header in allHeader:
    print("###For {} entropy calculation###".format(header))
    attributeClass = dataSet[header]
    AttriClassCountedValue = attributeClass.value_counts(sort=True).tolist() # need for calculating  specific attribute gain
    # print(AttriClassCountedValue)
    AttriClassIndex = attributeClass.value_counts(sort=True).index.tolist() #need for calculating frequeccy
    # print(AttriClassIndex)

    ##for loop is needed for outlook
    groupBy = dataSet.groupby([header, dependent]).size().reset_index(name="Time")
    #print(groupBy)

    for attrivalue in AttriClassIndex:
        specificAttriVal= groupBy.loc[ (groupBy[header]==attrivalue) ,'Time'].tolist()
        # print(specificAttriVal)
        while len(specificAttriVal) != maxDtClassElementLen:
            if len(specificAttriVal) == maxDtClassElementLen:
                break
            else:
                specificAttriVal.append(0)

        # print(specificAttriVal)

        sumOfAttriVal = sum(specificAttriVal)
        eachEntropy = 0
        print('I({}) ='.format(specificAttriVal), end='')
        for j in specificAttriVal:
            print('-({0}/{1})*log2({0}/{1})'.format(j, sumOfAttriVal), end='')
            try:
                eachEntropy  += -(j / sumOfAttriVal) * math.log2((j / sumOfAttriVal))
            except:
                eachEntropy = 0
        print('= {:.2f}'.format(eachEntropy))
        entropyLis.append(eachEntropy)
    entropyDict[header]= entropyLis
    entropyLis = list()
    print('')



############check#############

# entropyEachElements = entropyDict['wind']
# attributeClass = dataSet['wind']
#     # print(attributeClass)
# AttriClassCountedValue = attributeClass.value_counts(sort = True).tolist()
# sumOfAttriClassCountedValue = sum(AttriClassCountedValue)
# print(sumOfAttriClassCountedValue)
# probabilityCountedValue = list()
# for value in AttriClassCountedValue:
#     probabilityCountedValue.append(value/sumOfAttriClassCountedValue)
# sumresult = list()
# multiResult = 0
# print('{:.2f}'.format(dtClassEntropy),end='')
# for proba in range(len(probabilityCountedValue)):
#     multiResult += -(probabilityCountedValue[proba]*entropyEachElements[proba])
#     print('-({:.2f}*{:.2f})'.format(probabilityCountedValue[proba],entropyEachElements[proba]),end='')
# print('={:.2f}'.format(dtClassEntropy+multiResult))
#
#


###############check############


################ Gain Claculation #################
print('\n#################Information Gain Part#####################\n')
for i in allHeader:
    print('{} info gain: '.format(i))
    attributeClass = dataSet['{}'.format(i)]
    entropyEachElements = entropyDict[i]
    AttriClassCountedValue = attributeClass.value_counts(sort=True).tolist()
    sumOfAttriClassCountedValue = sum(AttriClassCountedValue)
    probabilityCountedValue = list()
    for value in AttriClassCountedValue:
        probabilityCountedValue.append(value / sumOfAttriClassCountedValue)
    sumresult = list()
    multiResult = 0
    print('{:.2f}'.format(dtClassEntropy), end='')
    for proba in range(len(probabilityCountedValue)):
        multiResult += -(probabilityCountedValue[proba] * entropyEachElements[proba])
        print('-({:.2f}*{:.2f})'.format(probabilityCountedValue[proba], entropyEachElements[proba]), end='')
    print('={:.2f}'.format(dtClassEntropy + multiResult))
    probabilityCountedValue = list()
    AttriClassCountedValue = 0

