import pandas as pd
import numpy as np
from multiprocessing.sharedctypes import Value

def right_split(arg):
    splitter = arg.split('-')
    res = int(splitter[1])
    return res

def between_values(arg):
    res = []
    splitter = arg.split('-')
    a = int(splitter[0])
    b = int(splitter[1])

    for i in range(a,b+1):
        res.append(i)

    return res

df = pd.read_csv('input.6.1.csv')

print('----------------','\n')

df1 = df.nlargest(1,'Цена')
a = df1['Наименование'].values[0]
b = df1['Цена'].values[0]
print('Самая дорогая игра:',a,', цена = ',b,'\n')

df2 = df['Год покупки'].value_counts()
print('Больше всего игр куплено в году:', df2.index[0],', количество игр:',df2.iat[0],'\n')

df3 = df['Издатель'].value_counts().head(3)    #.iloc[0:3]
print('Топ 3 издателей: \n', df3,'\n')

dict_players = {}
for index,value in df['Число игроков'].items():
    
    numbers_of_players = between_values(value)

    for numb in numbers_of_players:
        if numb not in dict_players:
            dict_players.setdefault(numb,1)
        else:
            dict_players[numb] += 1

max_value = max(dict_players.values())
final_dict = {k: v for k, v in dict_players.items() if v == max_value}
print('Какому количеству игроков легче всего подобрать игру : количество игр, в которую такая компания может сыграть\n',final_dict)


df['Макс'] = df['Число игроков'].map(right_split)
df5 = df[['Жанр','Макс']].groupby('Жанр').median()
df5.to_excel('6.1.Фамилия.xlsx')

df['Привлекательность'] = df['Реиграбельность'] - df['Сложность']
df = df.sort_values(by = 'Привлекательность',axis = 0, ascending = False)
print(df[['Наименование','Привлекательность']],'\n')

dict_mech = {}
for index, value in df['Механики'].items(): 
    list_mechs = str(value).split(',')
    list_mechs = map(lambda x: x.lower().replace(' ',''),list_mechs)
    for mech in list_mechs:
        if mech not in dict_mech:
            dict_mech.setdefault(mech,1)
        else:
            dict_mech[mech] += 1
print(dict_mech)





    

    

































