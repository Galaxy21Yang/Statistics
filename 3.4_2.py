from pylab import *
import numpy as np
data1 = [57, 29, 29, 36, 31,
         23, 47, 23, 28, 28,
         35, 51, 39, 18, 46,
         18, 26, 50, 29, 33,
         21, 46, 41, 52, 18,
         21, 43, 19, 42, 20]


data1.sort()
center = data1[(len(data1) - 1) // 2 - 3:(len(data1) - 1) // 2 + 2]
high = data1[(len(data1)-1)-5:(len(data1) - 1)]
low = data1[:5]
data = concatenate((data1, center, high, low), 0)
boxplot(data)
show()