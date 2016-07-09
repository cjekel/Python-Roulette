import numpy as np
import matplotlib.pyplot as plt

#   statistic simulation of winings over lots of games (stats for hackers)
import PythonRoulette
reload(PythonRoulette)
from PythonRoulette import *

import sys, os
#   turn off print
sys.stdout = open(os.devnull, 'w')

#banks = []
#startingBank = 100.00
#for j in range(0,100000):
#    play = roulette(rouletteStyle='American',bankAccount=startingBank)
#    for i in range(0,100):
#        play.roll(1,0)
#    banks.append(play.bankAccount)
##   restor print
#sys.stdout = sys.__stdout__
#
#banks = np.array(banks)
#banks = banks - startingBank
##   save the banks array
#np.save('banks', banks)
banks = np.load('banks.npy')
mean = np.mean(banks)
std = np.std(banks)
meanCentered = banks - mean
stdCentered = meanCentered / std

totalNumberOfPlays = 1000*1000
money = np.sum(banks)/totalNumberOfPlays

#   plot a histogram of the data
plt.figure()
plt.hist(stdCentered)
plt.show()

#   find the number of players that lost money or broke even
