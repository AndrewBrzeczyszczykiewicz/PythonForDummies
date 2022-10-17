import random

def calcHist(data):
    hist = [0] * 10
    for i in range(1000000):
        h = data[i] // 100
        if h > 9:
            hist[9] += 1
        else:
            hist[h] += 1
    return hist


def InitRList():
    rlist = []
    n = 1000000
    for i in range(n):
        rlist.append(random.randint(0, 999))
    return rlist


def histDistance(hist1, hist2) -> float:
    DRast = 0
    for i in range(10):
        DRast += (hist1[i] - hist2[i]) ** 2
    return DRast**(0,5)

def HWrite (hist1, hist2):
    f = open('glist.txt', 'w')
    f.write((str(hist1)) + '\n')
    f.write((str(hist2)) + '\n')
    f.close()

def HRead ():
    f = open('glist.txt', 'r')
    print(f.readlines())


hist1 = calcHist(InitRList())
hist2 = calcHist(InitRList())
print(histDistance(hist1,hist2))

HWrite(hist1, hist2)

HRead()






