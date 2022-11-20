import numpy as np
import random


def intr_sum(M):  # сумма внутренних элементов
    intr = 0
    for i in range (1,N-1):
        for j in range (1,N-1):
            intr += M[i][j]
    return intr


def extr_sum(M): # сумма внешних элементов
    extr = 0
    for i in range(N):
        if (i == 0 or i ==(N-1)): # первая или последняя строчка
            for j in range (N):
                extr += M[i][j]
        else:
            extr += M[i][0] + M[i][N-1]
    return extr


def main(N):
    fraction = -1
    count = 0
    iterations = 0
    if (N < 3):
        print("uncorrect N")
        return fraction
    elif (N > 9):
        print("uncorrect N")
        return fraction

    while iterations < 100000:

        M = [[random.randint(0,9) for j in range (N)] for i in range(N)]
        if extr_sum(M) > intr_sum(M):
            count += 1
        iterations += 1

    fraction = (count) / (100000)

    print("count = ", count)
    print("fraction = ", fraction)

    return fraction

#тело    
N = int(input())
main(N)










