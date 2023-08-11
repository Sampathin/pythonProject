#Normal distribution or gaussian // medical field
#Binomial distribution example: coin tossing,#n= number of trials,p-probality,#s -size of array
#Loc - mean (25/5 = 5)
#scale -standard deviation (graph plots ) ref mathsisfun.com
#size - size of array
#import matplotlib.pyplot as plt
from numpy import random
#x = random.normal(loc=5,scale=3,size=2)
y = random.binomial(n =4,p = 0.5,size=10)
#plt.show()
print(x)
print(y)