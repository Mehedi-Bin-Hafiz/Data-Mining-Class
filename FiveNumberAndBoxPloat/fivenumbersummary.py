from statistics import median
import matplotlib.pyplot as plt
import numpy as np


print("=====================Five number summary====================")

lis = [19, 23, 29, 31, 37, 41, 43, 47, 5, 7, 11, 13, 17]
lis.sort()
print('sorted list : ', lis)
Len = len(lis)
print(Len/2)
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
Min = Q1 - (1.5 * IQR)
Max = Q3 + (1.5 * IQR)

print('Min : ', Min)
print('Q1 : ', Q1)
print('Q2 : ', Q2)
print('Q3 : ', Q3)
print('Max : ', Max)


# Creating dataset
data = [Min, Q1, Q2, Q3, Max]

fig = plt.figure(figsize=(10, 7))
# Creating plot
plt.boxplot(data, vert=0)
plt.yticks([1, 2])
# show plot
plt.show()
