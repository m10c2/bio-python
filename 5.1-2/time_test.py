import random as rd
import numpy as np
import time


method1 = []
method2 = []

for i in range (10):
    number = rd.randint(0,9)

    start1 = time.perf_counter()
    #тут первый метод
    value = number*number
  
    method1.append(time.perf_counter() - start1)


    start2 =time.perf_counter()
    #тут второй метод
    value = number**2
    method2.append(time.perf_counter() - start2)

print(method1)
print("\n", method2)
