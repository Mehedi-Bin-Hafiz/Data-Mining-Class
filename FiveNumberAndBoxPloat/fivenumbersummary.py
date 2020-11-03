from statistics import median
import matplotlib.pyplot as plt
import numpy as np


print("=====================Five number summary====================")

lis = [19,21,28,40,51,55,59,61,70,72,74,87,90,97,98,99,99,110,117]
# lis = [20,23,28,40,48,55,59,65,70,72,74,80,90,97,98,99,99,110,115]
lis.sort()
print('sorted list : ', lis)
Len = len(lis)
Q2 = median(lis)


# ===================if odd number of elements
if Len % 2:
    Q1 = median(lis[: lis.index(Q2)])
    Q3 = median(lis[lis.index(Q2)+1:])

# ==================== if even number of elements
else:
    Q1 = median(lis[:int(Len/2)])
    Q3 = median(lis[int(Len/2):])


IQR = Q3 - Q1

LenRange = 1.5 ####

Min = Q1 - (LenRange * IQR)
Max = Q3 + (LenRange * IQR)


print('Q1 : ', Q1)
print('Q2 : ', Q2)
print('Q3 : ', Q3)
print ("IQR = {0}-{1}={2}".format(Q3,Q1,IQR))
print('Min : {0}-({1}*{2})={3}'.format(Q1,LenRange,IQR,Min))
print('Max : {0}+({1}*{2})={3}'.format(Q3,LenRange,IQR,Max))


# Creating dataset
data = [Min, Q1, Q2, Q3, Max]

fig = plt.figure(figsize=(10, 7))
# Creating plot
plt.boxplot(data, vert=0)
plt.yticks([1, 2])
# show plot
plt.show()
