#random numbers - rand(), randint(), choice
from numpy import random
x = random.rand(2)
y = random.randint(100)
yy = random.randint(100,size=5)
yyy = random.randint(100,size=(3,5))
z = random.choice([44,32,78,9,4,4,2,3])
zz = random.choice([44,32,78,9,4,4,2,3],size = (3,5))
print("Random Float Values\n",x)
print("Random int Values in 100\n",y,"\nRandom 5 int Values in 100\n",yy)
print("Random within given values\n",z,"\nRandom within given values and size\n",zz)
print("Random values within 100 with size\n",yyy)