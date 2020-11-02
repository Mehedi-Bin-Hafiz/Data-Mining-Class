import math

lis = [600,470,170,430,300]
length = len(lis)
print('total number: ',length)
print('sum: ',sum(lis))
Mean = sum(lis)/length
print("mean: {}/{} = {}".format(sum(lis),length,Mean))

dividelis=list()

for i in lis:
    dividelis.append(i-Mean)
print('need to squire and add each element: ',dividelis)

finaldividlis=list()
for i in dividelis:
    finaldividlis.append(i**2)

print('ans: ',finaldividlis )

variance= sum(finaldividlis)/length

print('variance: {:.2f}/{:.2f} = {:.2f}'.format(sum(finaldividlis),length,variance))

print('Standard deviation: root({})= {:.2f}'.format(variance,math.sqrt(variance)))

