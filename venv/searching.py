import numpy as np
#where method , returns index value of the specified element
x = np.array([1,2,3,5,7,2,8,3,9,3])
y = np.array([[6,2,3],[4,5,2]])
a = np.where(x ==3)
b = np.where(y ==2)
print(a)
print(b)

c = np.searchsorted(x,(5))
print(c)
