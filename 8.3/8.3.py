import numpy as np
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def compare(sym1, sym2):
    if sym1 == sym2:
        return 1
    else:
        return -1

def alignment(x, y, gap):
    ly = len(y)
    lx = len(x)

    F = [ [0]*(lx + 1) for _ in range (ly + 1)]

    for i in range(lx + 1):
        F[0][i] = gap*i
    for i in range(ly + 1):
        F[i][0] = gap*i

    for i in range (1, ly + 1):
        for j in range(1, lx + 1):
            diag = F[i-1][j-1] + compare(x[j-1],y[i-1])
            up = F[i-1][j] + gap
            left = F[i][j-1] + gap
            F[i][j] = max(diag, up, left)
    
    return F

def reverse(F,x,y,gap):
    i = len(y)
    j = len(x)
    al1, al2 = [],[]

    while (i != 0) or (j != 0):
        if (i != 0) and (F[i][j] == F[i-1][j] + gap):
            i -= 1
            al1.append('_')
            al2.append(y[i])
        
        elif (j != 0) and (F[i][j] == F[i][j-1] + gap):
            j -= 1
            al1.append(x[j])
            al2.append('_')
        
        else:
            i -= 1
            j -= 1
            al1.append(x[j])
            al2.append(y[i])
    
    return [''.join(al1[::-1]),''.join(al2[::-1])]

x = 'CATG'
y = 'ATGG'

print('manual','\n---------')
nw = alignment(x,y,-1)
steps = reverse(nw,x,y,-1)
print('score = ',nw[len(y)][len(x)])
print('steps =',steps,'\n')

print('-----------\n','pairwise','\n---------')
alignments = pairwise2.align.globalms(x, y, 1, -1, -1, -1)
print(format_alignment(*alignments[0]).replace(' ',''))
print(alignments)

