
def between(arg):
    res = []
    splitter = arg.split('-')
    a = int(splitter[0])
    b = int(splitter[1])

    for i in range(a,b+1):
        res.append(i)
    print(res)

    return
    

a = '2 - 22'
print(between(a))
