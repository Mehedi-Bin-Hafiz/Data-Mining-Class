
import matplotlib.pyplot as plt

def fivesum(Qnum,group,f,numofN=1,numofDivisor=2):

    x=list()
    for i in group:
        x.append((i[1]+i[0])/2)

    fx = list()
    for i in range(0,len(f)):
        fx.append(x[i]*f[i])

    fxsum=sum(fx)
    fsum=sum(f)
    print("{}   ->    {} ->   {}    ->  {}".format('group', 'f', 'x','fx'))
    for i in range(0, len(fx)):
        print("{:}  -> {:} -> {}  ->  {}".format(group[i], f[i], x[i],fx[i]))

    print("{:}      -> {:} -> {}  ->  {}".format(None, fsum, None,fxsum))


    cuf=list()
    inif = 0

    for i in f:
        inif=inif+i
        cuf.append(inif)
    print("\ncumulative frequency: ",cuf)

    selector= (numofN*fsum)/numofDivisor

    print('n/2: {}/{} = {}'.format(fsum,2,selector))
    medianclass=list()
    for i in group:
       if (i[0]<=selector and selector<=i[1]):
           medianclass.append([i[0],i[1]])
    print('median class:',medianclass)
    inx=group.index(medianclass[0])
    F=cuf[inx-1]
    print("F = ",F)
    fm=f[inx]
    print('fm= ',fm )

    precalss=group[inx-1]
    preclassval=precalss[1]
    realclass=group[inx]
    realclasval=realclass[0]
    Lm=(preclassval+realclasval)/2
    print('Lm: ({}+{})/2= {}'.format(preclassval,realclasval,Lm))

    i=realclass[1]-realclass[0]
    i = i+1
    print('i= ',i)

    Median = Lm + ((((numofN*fsum)/numofDivisor)-F)/fm)*i
    print('Median({}): {}+((({}*{})/{})-{})/{})*{}={:.2f}'.format(Qnum,Lm,numofN,fsum,numofDivisor,F,fm,i,Median))
    return Median


"""####Input Part####"""

group=[[1,10],[11,20],[21,30],[31,40],[41,50]]
f= [8,14,12,9,7]
Qnum='Q2'
numofN=1   ##3n,n
numofDivisor=2 ##3n/2  , n/2, n/4
print("\n###########Find Q2############")
Q2=fivesum(Qnum,group,f,numofN,numofDivisor)

Qnum='Q1'
numofN=1  ##3n,n
numofDivisor=4 ##3n/2  , n/2, n/4
print("\n###########Find Q1############")
Q1=fivesum(Qnum,group,f,numofN,numofDivisor)

Qnum='Q3'
numofN=3   ##3n,n
numofDivisor=4 ##3n/2  , n/2, n/4
print("\n###########Find Q3############")
Q3=fivesum(Qnum,group,f,numofN,numofDivisor)



"""####Result part####"""

IQR = Q3 - Q1
LenRange = 1.5 ####
Min = Q1 - (LenRange * IQR)
Max = Q3 + (LenRange * IQR)


print('Q1 : {0:.3f}'.format(Q1))
print('Q2 : {0:.3f}'.format(Q2))
print('Q3 : {0:.3f}'.format(Q3))
print ("IQR = {0:.3f}-{1:.3f}={2:.3f}".format(Q3,Q1,IQR))
print('Min : {0:.3f}-({1:.3f}*{2:.3f})={3:.3f}'.format(Q1,LenRange,IQR,Min))
print('Max : {0:.3f}+({1:.3f}*{2:.3f})={3:.3f}'.format(Q3,LenRange,IQR,Max))


# Creating dataset
data = [Min, Q1, Q2, Q3, Max]

fig = plt.figure(figsize=(10, 7))
# Creating plot
plt.boxplot(data, vert=0)
plt.yticks([1, 2])
# show plot
plt.show()





