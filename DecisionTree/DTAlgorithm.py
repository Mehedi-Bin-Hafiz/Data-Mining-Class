import pandas as pd
import tabula
import math



dataSet = pd.read_excel('examdata.xlsx')


################Declare entropy of decision class#############

dtClass = dataSet.play ##must assign decision class

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
########check#######

entropyLis = list()
entropyDict = dict()

for header in allHeader:
    print("###For {} calculation###".format(header))
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

# print(entropyDict['outlook'])





# ################ Gain Claculation #################
#
#
# for i in allHeader:
#     print('{} info gain: '.format(i))
#     attributeClass = dataSet['{}'.format(i)]
#     # print(attributeClass)
#     AttriClassCountedValue = attributeClass.value_counts(sort = True).tolist()
#     # print(AttriClassCountedValue)
#     sumOfCountedValue = sum(AttriClassCountedValue)
#     attriClassEntropy = 0
#
#     attibuteEntropy = entropyDict['{}'.format(i)]
#     gain = - dtClassEntropy
#     print('-{:.2f}'.format(dtClassEntropy),end='')
#     for j in range(len(AttriClassCountedValue)):
#         print(AttriClassCountedValue[j], attibuteEntropy[j])
#         gain += (-(AttriClassCountedValue[j]/sumOfCountedValue) * attibuteEntropy[j])
#         print(' -{:.2f}*{:.2f}'.format(dtClassEntropy,(AttriClassCountedValue[j]/sumOfCountedValue),attibuteEntropy[j],gain),end='')
#     print('= {:.2f}'.format(gain))
#


