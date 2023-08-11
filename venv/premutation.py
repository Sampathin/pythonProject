#shuffling
#permutation -
from numpy import random
import numpy as np
x = np.array([6,1,8,9,10,76,13])
y = np.array([76,21,38,49,10,96,63])
random.shuffle(x)
print("\nshuffle the values or change the values in declared variable\n",x,"\n")
yy = random.permutation(y)
print("shuffle or permutation wont change the values in declared variable but will be assigned in new variable\n",yy,"\n")
print("orginal value of variable with permutation\n",y)