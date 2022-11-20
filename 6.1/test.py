import pandas as pd
import numpy as np

def list_mn(arg):
    res = []

    splitter = arg.split('-')
    res.append(int(splitter[0]))
    res.append(int(splitter[1]))

    return res
    
def mn(ser):
    for i in range(len(ser)):
          ser[i] = np.mean(list_mn(ser[i]))
    return ser
        
df = pd.read_csv('input.6.1.csv')

ser = df['Число игроков']
ser = mn(ser)

print(ser.mean())





