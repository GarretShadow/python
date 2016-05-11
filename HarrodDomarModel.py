import math
import C:\Anaconda3\pylab
from matplotlib import mlab

from numpy import *
import matplotlib.pyplot as plt

#savingNorm - норма сбережения
#avrProdCapital - средняя производительность капитала
#release - начальное значение выпуска
#time - расчетный интервал


def HarrodDomarModel(savingNorm: float, avrProdCapital: float, initRelease: float, time: int):
    consum, invest = [], []
    release = [initRelease]
    for t in range(time+1):
        consum.append((1-savingNorm)*release[t])
        saving = savingNorm*release[t]#потребление капитала равно сумме сбережений
        invest.append(saving)
        release.append(release[t] + saving*avrProdCapital)



def familyRelease(avrProdCapital: list, initRelease: float):
    release = []
    for cap in range(len(avrProdCapital)):
        cRelease = [initRelease]
        t = 0
        for savingNorm in frange(0.1, 1.01, 0.1):
            cRelease.append(cRelease[t]*(1 + savingNorm*avrProdCapital[cap]))
            t += 1
        release.append(cRelease)
        cRelease.clear()

    return 0

HarrodDomarModel(0.7, 1.2, 80, 12)
familyRelease([1.2, 1.6, 1.8, 2.0], 80)
