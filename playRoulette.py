# let's play roulette
import PythonRoulette
reload(PythonRoulette)
from PythonRoulette import *

play = roulette(rouletteStyle='French',bankAccount=10.0)
for i in range(0,100):
    play.roll(1,0)
    if play.bankAccount == 0.0:
        break
        
