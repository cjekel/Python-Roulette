import numpy as np
import math
import matplotlib.pyplot as plt

#   what is the probability in roullette if placed 1000 times that the house looses money

#   define a function to do the n choose r math
def nChooseK(n,k):
    return(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
def subset(n, k): 
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return subset(n-1, k-1) + subset(n-1, k)
#   what are the total possible number of outcomes for 1000 bets betting 1 with payout 35:1 at odds 1:38
#totalPossiblity = 2**1000

#   for the casino, what is the number of wins a user needs on 1000 roles to not break even...

#   define a function that will calculate the money a house looses based on the number of wins
def houseMoney(nWins, n):
    #   negative means the house looses money
    houseMoneys = (1.*(n-nWins)) - (35.*nWins)
    return houseMoneys

money = houseMoney(28,1000)

#   what is the probability that on 1000 plays, the user wins at least 28 times
#   in other words, what is the probability the thouse looses money assuming a 
#   35:1 payout on American roulette
#   this can be done using the binomial distribution
def binomialDist(n,k,p):
    a = nChooseK(n,k)
    b = (p**k)*((1-p)**(n-k))
    return(a*b)
#   calculate the cumlative distribtion function:
pOfLoose = []
sumOfLoose = []
n = 1000
p = 1./38.
for i in range(0,1001):
    a = nChooseK(n,i)
    b = (p**i)*((1-p)**(n-i))
    pOfLoose.append(a*b)
    sumOfLoose.append(sum(pOfLoose))
    
expectedNumberOfWins = n*p
var = n*p*(1-p)
stdDev = math.sqrt(var)

print('The probability that the house will make money this month is ', sumOfLoose[28])
plt.figure()
plt.plot(pOfLoose)
plt.show()

plt.figure()
plt.plot(sumOfLoose)
plt.show()