# let's play roulette
import PythonRoulette
reload(PythonRoulette)
from PythonRoulette import *

play = roulette(rouletteStyle='French',bankAccount=10.0)
#for i in range(0,1):
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
#play.roulettyStyle = 'French'
#play.betType = 'Color'
#play.roll(1,'Black')

play.betType = 'Row'
play.roll(5)

#   I need to check if my Row bet type is legit, and if the payout is really 17 to 1
