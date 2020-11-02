import math
import statistics as st
from termcolor import colored

def customround(M):
    n = M - .50
    if n % 2 == 0:
        M = math.ceil(M)
    else:
        M = round(M)
    return M

def meanAlgo(a):

    m = st.mean(a)
    # print('--------------------------', m)
    m = customround(m)

    print(' Mean sliced array', a)
    print('array mean', m)

    for i in a:
        finalRes.append(m)


def boundaryAlgo(a):
    print(' Boundary sliced array', a, ' -> ',  end=' ')
    Min = min(a)
    Max = max(a)
    for i in a:
        if i-Min < Max-i:
            finalRes.append(Min)
            print(Min, end=' ')
        else:
            finalRes.append(Max)
            print(Max, end=' ')
    print()


x = 0
finalRes = []

a = [58, 65, 68, 69, 70, 71, 72, 73, 75, 75, 80, 81, 83, 85]
# a = [4, 8, 15, 21, 21, 24, 26, 30, 34]
a.sort()
Bin = 3  # ===========================================Bin size
Len = len(a)

'''  0 = mean algo //// 1 = boundary algo '''
typeOfAlgo = 1


while x < Len:
    if typeOfAlgo:
        boundaryAlgo(a[x:x+Bin])
    else:
        meanAlgo(a[x:x+Bin])
    x = x+Bin
print()
print()
finalRes = ' '.join(map(str, finalRes))
print(colored('final array ->  [ '+finalRes+' ]',
              'blue',
              # on_color='on_grey',
              attrs=['bold']))

