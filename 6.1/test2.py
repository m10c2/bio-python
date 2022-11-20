import numpy as np

def mean_pl(arg):
    splitter = arg.split('-')

    return np.mean(list(map(int,splitter)))

a = '2-22'

print(mean_pl(a))
