#i - integer
#b - boolen
#u - unsigned integer
#U - sunicode string
#f - float
#c - Complex float
#m - timedelta
#o - object
#M - datetime
#S - string
#V - null or (void)
import numpy as np
x = np.array([1,2,3,4],dtype ='S')
y = np.array([5,6,7,8])
z = np.array([9.9,4.4,4.4,2.2])
#z1 = np.array([9.9,4.4,4.4,2.2])
newy = y.astype("S")
newz = z.astype("i")
newz1 = z.astype("bool")
print(x.dtype)
print("Datatype",newy.dtype ,"\n",newy)
print("Before Datatype change",z.dtype ,"\n", z,"\nAfter Datatype change", newz.dtype, "\n",newz)
print(newz1)












