import random as rd
from genetic_сode import geneticCode

def shift(seq,n): #сдвиг
    l = len(seq)

    if n < 0:
        print('uncorrect n')
        return
    elif n > 2:
        print('uncorrect n')
        return

    if n == 1:
        seq = seq[1:]
    elif n == 2:
        seq = seq[2:]
        
    return seq

def start(seq, sub): #возвращает список с индексами старт - кодонов

    res = []
    count = seq.count(sub)
    ind = seq.find(sub)
 
    n_seq = seq
    f = n_seq.find(sub)
  

    while count > 0:
       
        res.append(ind)
        n_seq = n_seq[f+3:]

        f = n_seq.find(sub)
        ind += 3 + f   
        
        count -= 1

    print(res)
    return res

#def stop(seq):
    
nuct = ['A','T','G','C']

s_codon = 'ATG'

n = int(input())

l = rd.randint(5, 10)

randseq = [rd.choice(nuct) for j in range(l)]#посл. создается как список(sic!)
randseq = "".join(randseq)

print(randseq)

#counter = randseq.count('ATG')  #вот эта хуйня работает

print(start(randseq,s_codon))




  
