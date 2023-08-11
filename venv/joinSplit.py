import numpy as np
x = np.array([[1,2,3,4],[5,6,7,8]])
y = np.array([[11,12,33,44],[55,66,77,88]])
z = np.array([1,2,3,4,5,6,7,8])
a = np.squeeze((x,y))
b = np.concatenate((x,y),axis=1)
#print(a,"\n")
print(b)
sa = np.stack((x,y),axis=1)
sb = np.vstack((x,y))
sc = np.hstack((x,y))
print(sc)

sz = np.array_split(z  ,5)
print(sz[3])

#concatenate is join function, squeeze function get scaler , stack join in horizontal and vertical
#split function spilt single dimention to multi 