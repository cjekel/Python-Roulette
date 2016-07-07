import numpy as np
#   calculate the house odds

pWin = (1/38.)
pLoose = 1 - pWin
payOut = 35
EV = pWin*payOut - pLoose
#   expected net return on $100,000
print('Expected return on $100,000.00', 100000.00*EV)