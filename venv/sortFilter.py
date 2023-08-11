import numpy as np
x = np.array([6,7,4,8,2,3])
y = np.array([True,False,True,True,True,False])
z = x[y]
print(np.sort(z),z)#prints true values from the list with and without sort method
newz = []
for b in x:
    if b > 4:
      newz.append(True)
    else:
     newz.append(False)
c = x[newz]
print(c)
print(newz)
