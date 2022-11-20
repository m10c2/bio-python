
def counter(seq, sub):

    res = []
    count = seq.count(sub)
    ind = seq.find(sub)

    
    n_seq = seq
    f = n_seq.find(sub)
  

    while count > 0:
        print(ind)
        print(n_seq)
        res.append(ind)
        n_seq = n_seq[f+3:]
        f = n_seq.find(sub)
        ind += 3 + f   
        
        count -= 1
    print(res)

        
        
        
      
        
        
            
   
count = []   

test_seq = 'ATGTTATG'    
sub = 'ATG'


counter(test_seq,sub)


