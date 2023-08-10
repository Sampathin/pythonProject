#copy and view
import numpy as np
x = np.array([9,1,9,4,4,2,3,7,7,7,2,6])
y = x.copy()
x[0]= 0
print(x,"values from x")
print(y , "values from y")
z = x.view()
print(z,"replica activies of x")
