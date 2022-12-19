import math

def ex_unlimited(a,b,c):  #собственное исключение
    if (a == 0 and b == 0 and c == 0):
        raise RuntimeWarning("Unlimited number of roots")


def solving(file): #проверка корректоности входных данных
    try:
        with open(file, "r") as fin:

            root = []
            for line in fin:
                try:
                    splitter = line.split()
                    a = int(splitter[0])
                    b = int(splitter[1])
                    c = int(splitter[2])

                    ex_unlimited(a,b,c)

                    if a == 0:
                        if b!= 0:
                            x = (-c)/(b)
                            root.append([x])
                            print("x = %.2f" % x)
                        else:
                            root.append(["Корней нет"])
                            print("Корней нет")
                    else:
                        D = b ** 2 - 4 * a * c
                        if D > 0:
                            x1 = (-b + math.sqrt(D)) / (2 * a)
                            x2 = (-b - math.sqrt(D)) / (2 * a)
                            root.append([x1,x2])
                            print("x1 = %.2f x2 = %.2f" % (x1, x2))
                            
                        elif D == 0:
                            x = -b / (2 * a)
                            root.append([x])
                            print("x = %.2f" % x)
                        else:
                            root.append(["Корней нет"])
                            print("Корней нет")
                      
                except RuntimeWarning as e:
                        root.append(["Unlimited number of roots"])
                        print(e)

                except (ValueError, IndexError):
                    print('некорректные данные')
                    root.append(["некорректные данные"])
        
        return root 

                  
                    
    except FileNotFoundError:
        print("couldn't open the file", filename)
        return root
   


fin = 'input.4.1.txt'
fout = 'output.4.1.txt'

res = solving(fin)

res = [str(i) for i in res]

with open(fout, "w") as fout:

    for i in res:
        fout.write(i)
        fout.write('\n')







