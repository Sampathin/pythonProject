#n = number of possible outcomes , #pvals = more than 2 possibilities or list of probility
#multinominal example : Dice
from numpy import random
x = random.multinomial(n=6,pvals =[1/6,1/6,1/6,1/6,1/6],size=(10))
#you cant plot in seaborn model because of single dimension
print(x)