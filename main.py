import random
import time

def calcHist(data):
    hist = [0]*10
    for i in range (1000000):
        h = data[i] // 100
        if h>9:
            hist[9]+=1
        else:
            hist[h] += 1
    return hist

def InitRList():
    rlist =[]
    n = 1000000
    for i in range(n):
        rlist.append(random.randint(0,999))
    return rlist

total = 0
min = 1
max = 0
for i in range (99):
    x= InitRList()
    start = time.time()
    calcHist(x)
    end = time.time()
    total = total + (end - start)
    if (end-start) > max:
        max = (end-start)
    if (end-start) < min:
        min = (end-start)

print('Среднее время',total/100)
print('Минимальное время', min)
print('Максимальное время', max)

