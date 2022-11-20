import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import random as rd 
def makeplot(s):
    nucl = {}
    for nuc in 'ATGC':
        nucl[nuc] = s.count(nuc)
    codons = {}
    for i in range(0,len(s)-2,3):
        codon = s[i:i+3]
        if codon in codons:
            codons[codon] +=1
        else:
            codons[codon] = 1

    gridform = (2,2)
    ax1 = plt.subplot2grid(gridform, (0,0))
    ax2 = plt.subplot2grid(gridform, (0,1))
    ax3 = plt.subplot2grid(gridform, (1,0))
    ax4 = plt.subplot2grid(gridform, (1,1))
   
    
    ax1.bar(nucl.keys(), nucl.values())
    ax2.pie(nucl.values(), labels = nucl.keys())
    ax3.hist(codons.values(), bins=10)
    ax4.boxplot(codons.values())

    plt.show()
    
#n = rd.randint(100,100)
n = 1000
seq = ""
for i in range(n):
    seq = seq + rd.choice('ATGC')
print(seq)
print(len(seq))
makeplot(seq)