# let's play roulette
import PythonRoulette
reload(PythonRoulette)
from PythonRoulette import *

#import sys, os
##   turn off print
#sys.stdout = open(os.devnull, 'w')
##   restore print
#sys.stdout = sys.__stdout__ 

#play = roulette(rouletteStyle='American',bankAccount=100000.0)
#for i in range(0,1000000):
#    play.roll(1,0)
#    if play.bankAccount == 0.0:
#        break
#play.rouletteStyle='American'
#play.roll(1,-1)

      
play = roulette(rouletteStyle='American', bankAccount=150.0, betType='Color')

#play.roll(50,'Black')
#        
#play.betType = 'Straight'
#play.roll(100, -1)
play.rouletteStyle = 'French'
#play.betType = 'Color'
#play.roll(1,'Black')

#play.betType = 'Row'
#play.roll(5)


#play.betType = 'Split'
#play.roll(50,[1,9])

#play.betType = 'Street'
#play.roll(5,[1,2,-1])

#play.betType = 'Corner'
#play.roll(5,[1,0,2,36])

#play.betType = 'Line'
#play.roll(5,[-1,0,1,3,4,5])

#play.betType = 'Dozen'
#play.roll(5,[2,0,1,3,4,5,6,7,8,9,10,11])

#play.betType = 'Penta'
#play.roll(5, [1,2,3,4,-1])

play.betType = 'EvenOdd'
play.roll(5, 'Even')



##   plot roll history
#import matplotlib.pyplot as plt
#bins = range(-1, 38)
#plt.figure()
#plt.hist(play.rollHistory, bins)
#plt.title('The roll histogram')
#plt.xlabel('Number rolled')
#plt.ylabel('Quantity of rolls')
#plt.show()
