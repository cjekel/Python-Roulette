# let's play roulette
import PythonRoulette
reload(PythonRoulette)
from PythonRoulette import *

play = roulette(rouletteStyle='French',bankAccount=10.0)
#for i in range(0,1):
#    play.roll(1,0)
#    if play.bankAccount == 0.0:
#        break
        
play = roulette(rouletteStyle='American', bankAccount=100.0, betType='Color')

play.roll(50,'Black')
        
