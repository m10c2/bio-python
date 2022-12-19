import random as rd
from genetic_code import geneticCode

def sep_to_triplets(seq):
    triplets = [seq[x:x+3] for x in range(0, len(seq), 3)]

    if triplets == []:
        return triplets
    
    if len(triplets[- 1]) != 3:
        triplets.pop()    
    
    return triplets

"возвращает индекс первого старт кодона, -1 если не нашлось"
def find_start(triplets):
    for triplet in triplets:
        if (geneticCode[triplet] == 'M'):
            return triplets.index(triplet)
    return -1

"возвращает индекс первого стоп кодона, -1 если не нашлось"
def find_stop(triplets):
    for triplet in triplets:
        if (geneticCode[triplet] == None):
            return triplets.index(triplet)
    return -1

"трансляция"
def decode(triplets):
    res = []
    for triplet in triplets:
        if geneticCode[triplet] != None:
            res.append(geneticCode[triplet])
    return ''.join(res)

def orf(frame, seq, res=None, str_start=0):
    if res == None:
        res = []
    triplets = sep_to_triplets(seq)
    if (triplets == []):
        return res

    start_i= find_start(triplets)
    stop_i = find_stop(triplets)

    if (start_i != -1) and (stop_i != -1):

        if start_i < stop_i: #complete  1
            r_seq = "".join(decode(triplets[start_i:stop_i]))
            
            start = str_start + start_i*3 + frame
            stop = str_start + stop_i*3 + frame
            str_start += len("".join(triplets[:stop_i+1]))
            
            res.append((r_seq, 'complete', start, stop))
            
            seq = "".join(triplets[stop_i+1:])
            orf(frame, seq, res, str_start)
        
        elif start_i > stop_i: #stop  3
            r_seq = "".join(decode(triplets[:stop_i]))

            start = str_start + frame
            stop = str_start + stop_i*3 + frame
            str_start += len("".join(triplets[:stop_i+1])) 
            
            res.append((r_seq, 'stop', start, stop))
            
            seq = "".join(triplets[stop_i+1:])
            orf(frame, seq, res, str_start)
    
    elif (start_i != -1) and (stop_i == -1): 
        r_seq = "".join(decode(triplets[start_i:]))
        
        start = str_start + start_i*3 + frame
        stop = str_start + len(triplets)*3 + frame
        str_start += len("".join(triplets[:start_i]))
      
        res.append((r_seq, 'start', start, stop)) # 2 start

        seq = ""
        orf(frame, seq, res, str_start)
    
    elif (start_i == -1) and (stop_i != -1):#найден стоп без старта
        r_seq = "".join(decode(triplets[:stop_i]))

        start = str_start + frame
        stop = str_start + stop_i*3 + frame
        str_start += len("".join(triplets[:stop_i+1]))
        
        res.append((r_seq, 'stop', start, stop)) #3 stop

        seq = "".join(triplets[stop_i+1:])
        orf(frame, seq, res, str_start)
    
    elif (start_i == -1) and (stop_i == -1):
        r_seq = "".join(decode(triplets))
        
        start = str_start + frame
        stop = str_start + (len(triplets) - 1)*3 + frame
        str_start += len("".join(triplets))
        
        res.append((r_seq, 'empty', start, stop)) #4 empty

        seq = ""
        orf(frame, seq, res, str_start)
    
    return res

def find_orf(seq,frame):
    return orf(frame, seq[frame:])
    

def data_from_file(file_name):
    
    with open(file_name, encoding="latin1") as f:
            text = f.read()
            indents = text.split(">")

    data = []
    indents = indents[1:]

    for indent in indents:
        lines = indent.split("\n")
        header = lines[0]
        seq = "".join(lines[1:]).strip()
        data.append((header, seq))
        
    return data

def record(fin, fout):
    data = data_from_file(fin)
    with open(fout, "w") as fout:

        for seq in data:
            for frame in [0,1,2]:
                seq_orfs = find_orf(seq[1], frame)
                for seq_orf in seq_orfs:
                    output = f">{seq[0]}|frame:{frame}, type:{seq_orf[1]}, start:{seq_orf[2]}, stop:{seq_orf[3]},\n{seq_orf[0]}"
                    fout.write(output)
                    fout.write("\n\n")
                    print(output,'\n\n')
                    
                    
f1 = 'input.4.2.txt'
f2 = 'output.4.2.txt'

record(f1,f2)

seq = 'AAATTTTGAAAAATGTTTTAATTTGTTGTATGAAAAATGAAA'
#print(find_orf(seq, 0))









