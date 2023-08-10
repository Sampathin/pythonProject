import numpy as np
def intro():
    x = np.array([1,2,3,4,5])
    print(x)
    #print(np.dtype)
    print(np.__dir__())
intro()
def Dim():
    x0 = np.array(36)
    x1 = np.array([1,2,3])
    x2 = np.array([[1,2,3],[4,5,6]])
    x3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
    x4 = np.array([1,2,3],ndmin=5)
    print(x4.ndim)
Dim()
def indexing():
    x = np.array([1,2,3,4,5,6,7,8])
    print(x[-1],x[4])
    y = np.array([[1,2,3],[4,5,6]])
    print(y[0,2],y[1,1])
indexing()
def data_types():
    #i=int,S=string,f=float,c=complex,U=uniinteger,V=unsigned
    x = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
    print(x.dtype)
    y = x.astype(dtype='S')
    print("print datatype\n", y.dtype,"\n",y)
data_types()
def shapes():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([[[1,2,3,4],[4,5,6,7],[7,8,9,10]]])
    z = np.array([[[1,2],[4,5],[7,8]]])
    print(x.shape)
    print(z.shape,z)
    print(y.shape,y)
    print(y.reshape(2,3,2))
shapes()
def copyViews():
    x = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
    y = np.array([[[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]]])
    b = x.copy()
    c = y.copy().astype('i')
    d = y.view()

    print(b)
    print(c.dtype,y.dtype,c)
    print(d.astype('i') ,y)
copyViews()
