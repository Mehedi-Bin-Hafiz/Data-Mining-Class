TP = 59
TN = 12
FP = 27
FN = 2

accuracy = (TP+TN)/(TP+TN+FP+FN)
print('Accuracy = ({0}+{1})/({0}+{1}+{2}+{3}) = {4:.3f}'.format(TP,TN,FP,FN,accuracy))
error =  1-accuracy
print('Error= 1 - {0}= {1:.3f}'.format(accuracy,error))

print('\n####Rate####')
print('TP Rate: {0}/({0}+{1}) = {2:.3f}'.format(TP,FN,(TP/(TP+FN))))
print('FP Rate: {0}/({0}+{1}) = {2:.3f}'.format(FP,TN,(FP/(FP+TN))))
print('TN Rate: {0}/({0}+{1}) = {2:.3f}'.format(TN,FP,(TN/(TN+FP))))
print('FN Rate: {0}/({0}+{1}) = {2:.3f}'.format(FN,TP,(FN/(FN+TP))))


print('\n###Precision###')
PreTP=(TP/(TP+FP))
PreTN=(TN/(TN+FN))
print('For TP ={0}/({0}+{1})= {2:.3f}'.format(TP,FP,PreTP))
print('For TN ={0}/({0}+{1})= {2:.3f}'.format(TN,FN,PreTN))
# print('Weighted average ={:.2f}'.format((PreTP+PreTN)/2))

print('\n###Recall###')

ReTP=(TP/(TP+FN))
ReTN=(TN/(TN+FP))
print('For TP ={0}/({0}+{1})= {2:.3f}'.format(TP,FN,ReTP))
print('For TN ={0}/({0}+{1})= {2:.3f}'.format(TN,FP,ReTN))
# print('Weighted average ={:.2f}'.format((ReTP+ReTN)/2))


print('\n###F-Measure###')
ans2 =  ((2*PreTP*ReTP)/(PreTP+ReTP))
print('For TP =({0}*{1:.2f}*{2:.2f})/({1:.2f}+{2:.2f})= {3:.3f}'.format(2,PreTP,ReTP,ans2))
ans1 =  ((2*PreTN*ReTN)/(PreTN+ReTN))
print('For TN =({0}*{1:.2f}*{2:.2f})/({1:.2f}+{2:.2f})= {3:.3f}'.format(2,PreTN,ReTN,ans1))

# print('Weighted average ={:.2f}'.format((ReTP+ReTN)/2))


print("\nWhich detection is better for our model?")

TotalTRUE = TP+FN
des=TP/TotalTRUE
TotalFalse = TN+FP
des2 = TN/TotalFalse
if des>des2:
    print("This model is better for positive prediction")
else:
    print("This model is better for negative prediction")







