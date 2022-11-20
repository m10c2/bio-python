import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import random as rd 
import numpy as np

alphabet_dict = {'A':'A','T':'T','G':'G','C':'C','AT':'W','AG':'R',
                'AC':'M','TG':'K','TC':'Y','GC':'S','TGC':'B','AGC':'V',
                'ATC':'H','ATG':'D','ATGC':'N'}

nucl = {0:'A', 1:'T', 2:'G', 3:'C', 4:'W',5:'R',6:'M',7:'K',8:'Y',9:'S',10:'B',
        11:'V',12:'H',13:'D',14:'N'}

def symbol_count(column):
    res = []
    for j in 'ATGC':
        res.append(column.count(j))
    return res

def get_indices(arr, el):
    result = []
    for i in range(len(arr)):
        if arr[i] == el:
            result.append(i)
    return result

def transform(freq_arr):
    freq_arr = np.array(freq_arr)
    pre_seq1 = []
    for i in range(9):
        pre_seq1.append(get_indices(freq_arr[i],freq_arr[i].max()))

    pre_seq2 = [[] for i in range (9)]
    for i in range (9):
        for j in range (len(pre_seq1[i])):
            pre_seq2[i].append(nucl[pre_seq1[i][j]])

    result = []
    for i in range (len(pre_seq2)):
        result.append(''.join(pre_seq2[i]))

    return result 

def decode(pre_seq):
    result = []
    for i in range (len(pre_seq)):
        result.append(alphabet_dict[pre_seq[i]])
    return result

def letter_counter(word):
    stats = dict()
    word = word.strip()
    for symbol in word:
        if symbol in stats:
            stats[symbol] += 1
        else:
            stats[symbol] = 1
    return stats

print('\n_________________________','\n')
db = []
with open('input.7.2.txt','r') as file:
    for line in file:
        db.append(line.strip())

freq = []
for i in range(9):
    freq.append(symbol_count([x[i] for x in db]))

f = np.transpose(np.array(freq))

ind = [0,1,2,3,4,5,6,7,8]
fig = plt.figure()
ax1 = fig.add_subplot(211)

ax1.bar(ind,f[0],color = 'blue',label = 'A')
ax1.bar(ind,f[1],bottom = f[0], color = 'orange',label = 'T')
ax1.bar(ind,f[2],bottom = f[0] + f[1], color = 'red',label = 'G')
ax1.bar(ind,f[3],bottom = f[0] + f[1] + f[2], color = 'green',label = 'C')
ax1.legend()

seq = ''.join(decode(transform((freq))))
print('консенсусная последовательность:',seq)

stats = letter_counter(seq)
nucl_freq = []

for i in range(15):
    if nucl[i] in stats:
        nucl_freq.append(stats[nucl[i]]/15)
    else:
        nucl_freq.append(0)

labels = ['A','T','G','C','W','R','M','K','Y','S','B',
        'V','H','D','N']
dataLabels = [labels[i] if (nucl_freq[i] != 0) else '' for i in range (15)]
explode = [0.1]*15
ax2 = fig.add_subplot(212)
ax2.pie(nucl_freq,labels = dataLabels,explode = explode)

plt.show()




    