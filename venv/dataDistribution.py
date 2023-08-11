#probabilities / changes feeding
#assigned as "p" which means random.choice([values]),p[0 -1 ],size())
#probability values should upto value 1.0 with addition of all values
#something like 0.1,0.3,0.4,0.2 - so total 1.0
from numpy import random
x = random.choice([7,4,6,9,3],p=[0.3,0.2,0.4,0.1,0.0],size=[100])
print(x)
y = random.choice([7,4,6,9,3],p=[0.3,0.2,0.4,0.1,0.0],size=[3,5])
print(y)