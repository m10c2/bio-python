import time
import random as rd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def manual(a,b,size):  #функция для ручного умножения
    c = [[0]*size for i in range(size)]
    for i in range (size):
        for j in range(size):
            for k in range(size):
                c[i][j] += a[i][k]*b[k][j]
    return c

def comparsion():
    
    graph1 = []  #это списки для графиков
    graph2 = []

    for N in range (1,8):

        X = np.random.randint(0,9,(2**N,2**N))
        Y = np.random.randint(0,9,(2**N,2**N))

        method1 = []
        method2 = []

        avr = [] #среднее время
        sgm = [] #среднее отклонение

        for k in range(100):
            start1 = time.perf_counter()
            C_numpy = np.dot(X,Y)
            method1.append(time.perf_counter()- start1)
        
            start2 = time.perf_counter()
            C_manual = manual(X,Y,N)
            method2.append(time.perf_counter() - start2)

        avr.append([np.mean(method1)]) #numpy  
        avr.append([np.mean(method2)]) #manual

        sgm.append([np.std(method1)])   #numpy
        sgm.append([np.std(method2)])   #manual

        graph1.append(method1[2])       #два графика для каждого умножения
        graph2.append(method2[2])

        
        print("\nN = ",N)

        print("average numpy time = ", avr[0])
        print("devitation numpy time = ", sgm[0])

        print("\naverage manual time = ", avr[1])
        print("devitation manual time = ", sgm[1])

        if avr[0] > avr[1]:
            print("\nmanual")
        elif avr[0] < avr[1]:
            print("\nnumpy")
        else:
            print("удивительно")
    
    return graph1,graph2  #возвращаем в виде кортежа


#main
gr1, gr2 = comparsion() # numpy , manual

#дальше графики
fig = plt.figure()
ax = fig.add_subplot(111)

#редактирование делений
plt.xticks([0,1,2,3,4,5,6],['$2^1$','$2^2$','$2^3$','$2^4$','$2^5$','$2^6$','$2^7$'])

#добавление легенды
plt.plot(gr1, label = 'numpy')
plt.plot(gr2, label = 'manual')
plt.legend(fontsize=14)

#логарифмирование времени
plt.semilogy() 


#подписи к осям
plt.xlabel('matrix size', fontsize=12)
plt.ylabel('time on 3rd step',fontsize=12)


plt.show()

        

    
    
    
