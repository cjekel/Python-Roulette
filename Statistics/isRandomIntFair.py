import random
import matplotlib.pyplot as plt

lowerBound = -1
upperBound = 36
rolls = 100000

randomInts = []
for i in range(0, rolls):
    randomInts.append(random.randint(lowerBound, upperBound))

#   create histogram plot
plt.figure()
bins = range(lowerBound-1, 2+upperBound)
plt.hist(randomInts, bins)
plt.xlabel('Bins')
plt.ylabel('number of times rolled')
plt.title('histogram of randint')
plt.show()

#   it appears randint is fair