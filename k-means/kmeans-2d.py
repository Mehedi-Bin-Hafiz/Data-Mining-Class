from statistics import mean
from termcolor import colored

# lx = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
# ly = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]

lx = [1, 1.5, 3.0, 5.0, 3.5, 4.5, 3.5]
ly = [1, 2.0, 4.0, 7.0, 5.0, 5.0, 4.5]

# number of clusters
k = 2

cx1 = 0
cxn1 = 1

cy1 = 0
cyn1 = 1

cx2 = 0
cxn2 = 5

cy2 = 0
cyn2 = 7

lx1 = []
lx2 = []

ly1 = []
ly2 = []

while cx1 != cxn1 and cx2 != cxn2 and cy1 != cyn1 and cy2 != cyn2:
    cx1 = cxn1
    cx2 = cxn2
    cy1 = cyn1
    cy2 = cyn2
    tlx1 = []
    tlx2 = []
    tly1 = []
    tly2 = []
    print()
    print()
    print()
    print('cx1 = ', f'{cx1:4.2f}', 'cx2 = ', f'{cx2:4.2f}')
    print('cy1 = ', f'{cy1:4.2f}', 'cy2 = ', f'{cy2:4.2f}')
    print()

    print(colored('x     ', 'red'),
          colored('cx1   ', 'blue'),
          colored('cy1   ', 'green'),
          colored('cx2   ', 'blue'),
          colored('cy2   ', 'green'),
          colored('Dis1  ', 'cyan'),
          colored('Dis2  ', 'magenta'),
          'class')

    print()

    for i, j in zip(lx, ly):
        Distance1 = ((i - cx1) ** 2 + (j - cy1) ** 2) ** .5
        Distance2 = ((i - cx2) ** 2 + (j - cy2) ** 2) ** .5
        if Distance1 <= Distance2:
            tlx1.append(i)
            tly1.append(j)
            # print('{}  {} {} {} {} {}'.format(i, c1, c2, c1Distance, c2Distance, 1))
            print('{}{}{}{}{}{}{}    {}'.format(colored(f'{i:4.2f}', 'red'),
                                            colored(f'{cx1:7.2f}', 'blue'),
                                            colored(f'{cx2:7.2f}', 'green'),
                                            colored(f'{cy1:7.2f}', 'blue'),
                                            colored(f'{cy2:7.2f}', 'green'),
                                            colored(f'{Distance1:7.2f}', 'cyan'),
                                            colored(f'{Distance2:7.2f}', 'magenta'),
                                            colored(1, 'red')))
        else:
            tlx2.append(i)
            tly2.append(j)
            # print('{}  {} {} {} {} {}'.format(i, c1, c2, c1Distance, c2Distance, 2))
            print('{}{}{}{}{}{}{}    {}'.format(colored(f'{i:4.2f}', 'red'),
                                            colored(f'{cx1:7.2f}', 'blue'),
                                            colored(f'{cx2:7.2f}', 'green'),
                                            colored(f'{cy1:7.2f}', 'blue'),
                                            colored(f'{cy2:7.2f}', 'green'),
                                            colored(f'{Distance1:7.2f}', 'cyan'),
                                            colored(f'{Distance2:7.2f}', 'magenta'),
                                            colored(2, 'blue')))

    if lx1 != tlx1:
        lx1 = tlx1
        ly1 = tly1
        cxn1 = mean(tlx1)
        cyn1 = mean(tly1)
    if ly2 != tly2:
        lx2 = tlx2
        ly2 = tly2
        cxn2 = mean(tlx2)
        cyn2 = mean(tly2)

    print('=============================l1 cxn1 = ', f'{cxn1:4.2f}', '  cyn1 = ' f'{cyn1:4.2f}')
    print(lx1)
    print(ly1)
    print()
    print('============================= l2 cxn2 = ', f'{cxn2:4.2f}', '  cyn2 = ' f'{cyn2:4.2f}')
    print(lx2)
    print(ly2)
    print()
    print()

print()
print()
print()
print()

print('============================= final l1')
print(lx1)
print(ly1)
print('============================= final l2')
print(lx2)
print(ly2)
