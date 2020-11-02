a = [4, 5, 3, 5, 6, 7, 8, 12, 23, 56, 34, ]
a.sort()
print('Sorted List=',a)
min = min(a)
max = max(a)
dif = max - min

###Enter given range###
newMax = 1
newMin = 0
print('(v-min)/(max-min)*(newMax - newMin) + newMin =  v!')

lis =list()
for x in a:
    res = (x-min)/(max-min)*(newMax - newMin) + newMin
    print('({1} - {2}) / ({3} - {2}) * ({4} - {5}) + {5} = {0:.2f} '.format(res, x, min, max, newMax, newMin))
    lis.append(float('{:.2f}'.format(res)))

print('before normalization:', a)
print('after normalization:',lis)

