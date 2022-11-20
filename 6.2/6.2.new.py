from cmath import nan
import pandas as pd
import numpy as np
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

def is_cons(seq,index_list): 
    i = 0
    for x in seq:
        if x in index_list[i]:
            i += 1
        else:
            return False
    return seq
    
def get_ind_col(df_column,value):
    index_list = list()
    P = df_column.isin([value])
    rows = list()   
    rows = list((P[P == True]).index)

    for row in rows:
        index_list.append(row) 
   
    return index_list

def get_ind(dfObj, value):

    listOfPos = list()
    result = dfObj.isin([value])
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            if row in listOfPos:
                continue
            else:
                listOfPos.append((row))
    return listOfPos

def dist(seq1,seq2):
    res = 0
    i = 0
    for x in seq1:
        if x == seq2[i]:
            i += 1
        else:
            res += 1
            i += 1
    return (res / 10)

def dist_JC(seq,p): 
    a = (1 - (4*p)/3)
    if (a <= 0):
        return nan
    else:
        return (-3/4)*np.log(a)

def count_P(seq1,seq2):
    P = 0
    i = 0
    for x in seq1:
        if (x == 'A' and seq2[i] == 'G') or (x == 'G' and seq2[i] == 'A') or (x == 'C' and seq2[i] == 'T') or (x == 'T' and seq2[i] == 'C'):
            P += 1
            i += 1
        else:
            i += 1
    return P

def count_Q(seq1,seq2):
    Q = 0
    i = 0
    for x in seq1:
        if ((x == 'A' or x =='G') and (seq2[i] == 'C' or seq2[i] == 'T')) or ((x == 'C' or x == 'T') and (seq2[i] == 'A' or seq2[i] == 'G')):
            Q += 1
            i += 1
        else:
            i += 1
    return Q

def dist_K2P(seq1,seq2):
    P = count_P(seq1,seq2) / 10
    Q = count_Q(seq1,seq2) / 10
    if ((1 - 2*P - Q) <= 0) or ((1 - 2*Q) <= 0):
        return nan
    else:
        return ((-1/2)*np.log(1 - 2*P - Q) - (1/4)*np.log(1 - 2*Q))

def category(arg,a,b):
    if arg in a:
        return True
    elif arg in b:
        return False
  
df = pd.read_excel('input.6.2.xlsx')
df_sep = pd.DataFrame()

for i in range(10):
    df_sep[str(i)] = df['sequence'].map(lambda x: x[i])

df_freq = df_sep[['0','1','2','3','4','5','6','7','8','9']].apply(pd.Series.value_counts)
cons = [[] for i in range (10)]

for i in range(10):
    max_ = int(df_freq[str(i)].max())
    cons[i] = get_ind_col(df_freq[str(i)],max_)

df_cons = df['sequence'].map(lambda x:is_cons(x,cons)) #работает !
cons_seq = list(df_cons[df_cons != False])[0]

df['dist'] = df['sequence'].map(lambda x:dist(x,cons_seq))
df['d_JC'] = df['sequence'].map(lambda x:dist_JC(x,dist(x,cons_seq)))
df['d_K2P'] = df['sequence'].map(lambda x: dist_K2P(x,cons_seq))

print('-------------------------------------')

df_a = df.dropna(axis = 0)

no_nan_rows = list(df_a.index)
df_b = df.drop(axis = 0, labels = no_nan_rows)

nan_rows = list(df_b.index)
rows = list(df.index)

cat = []
for x in rows:
    if x in no_nan_rows:
        cat.append(True)
    elif x in nan_rows:
        cat.append(False)

df['ab'] = cat
df['ab'].replace(
    {True: "Yes", False: "No"}, 
    inplace=True)

ax = sns.violinplot(x = df['ab'], y=df['dist'])
ax.get_figure().savefig('violin.png')









        











  









