from statistics import mean
from termcolor import colored

l = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]

# number of clusters
k = 2

c1 = 0
cn1 = 16

c2 = 0
cn2 = 22

l1 = []
l2 = []

while c1 != cn1 and c2 != cn2:
    c1 = cn1
    c2 = cn2
    tl1 = []
    tl2 = []
    print('c1 = ', c1, 'c2 = ', c2)
    print()

    print(colored('x   ', 'red'),
          colored('c1   ', 'blue'),
          colored('c2   ', 'green'),
          colored('c1Distance    ', 'cyan'),
          colored('c2Distance    ', 'magenta'),
          'class')

    print()

    for i in l:
        c1Distance = abs(i - c1)
        c2Distance = abs(i - c2)
        if c1Distance < c2Distance:
            tl1.append(i)
            # print('{}  {} {} {} {} {}'.format(i, c1, c2, c1Distance, c2Distance, 1))
            print('{}    {}    {}     {}    {}    {}'.format(colored(i, 'red'),
                                                             colored(c1, 'blue'),
                                                             colored(c2, 'green'),
                                                             colored(c1Distance, 'cyan'),
                                                             colored(c2Distance, 'magenta'),
                                                             1))
        else:
            tl2.append(i)
            # print('{}  {} {} {} {} {}'.format(i, c1, c2, c1Distance, c2Distance, 2))
            print('{}    {}    {}     {}    {}    {}'.format(colored(i, 'red'),
                                                             colored(c1, 'blue'),
                                                             colored(c2, 'green'),
                                                             colored(c1Distance, 'cyan'),
                                                             colored(c2Distance, 'magenta'),
                                                             2))

    if l1 != tl1:
        l1 = tl1
        cn1 = mean(tl1)
    if l2 != tl2:
        l2 = tl2
        cn2 = mean(tl2)

    print('=============================l1 with cn1=', cn1)
    print(l1)
    print('=============================l2 with cn2=', cn2)
    print(l2)
    print()
    print()

print()
print()
print()
print()

print('============================= final l1')
print(l1)
print('============================= final l2')
print(l2)
