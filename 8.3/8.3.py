import numpy as np
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

r = lambda x,y,i,j: -1 if x[i] != y[j] else 1

def find_solution(OPT, m, n): # m = lenx, n = leny

    if m == 0 or n == 0:
        return
    
    insert = OPT[m][n - 1] - 1 if n != 0 else float("inf")
    align = (
            OPT[m - 1][n - 1] + r(x, y, m - 1, n - 1)
            if m != 0 and n != 0
            else float("inf"))
    delete = OPT[m - 1][n] - 1 if m != 0 else float("inf")

    best_choice = max(insert, align, delete)

    if best_choice == insert:
            solution.append("insert_" + str(y[n - 1]))
            return find_solution(OPT, m, n - 1)

    elif best_choice == align:
            solution.append("align_" + str(y[n - 1]))
            return find_solution(OPT, m - 1, n - 1)

    elif best_choice == delete:
        solution.append("remove_" + str(x[m - 1]))
        return find_solution(OPT, m - 1, n)
 
def alignment(x, y, gap):
    ly = len(y)
    lx = len(x)

    OPT = [[0 for i in range(ly + 1)] for j in range(lx + 1)]

    for i in range(1, lx + 1):
        OPT[i][0] = -i
    for j in range(1, ly + 1):
        OPT[0][j] = -j

    for i in range (1, lx + 1):
        for j in range(1, ly + 1):
            OPT[i][j] = max(OPT[i-1][j-1] + r(x,y,i-1,j-1), OPT[i-1][j] + gap, OPT[i][j-1] + gap)

    find_solution(OPT,lx,ly)
    return (OPT[lx][ly], solution[::-1])

x = 'GG'
y = 'ATGG'

solution = []

nw, solution  = alignment(x,y,-1)
print('\nresult = ', nw)
print('steps = ', solution)

alignments = pairwise2.align.globalms(x, y, 1, -1, -1, -1)
print('\n',format_alignment(*alignments[0]).replace(' ',''))
print(alignments)





















