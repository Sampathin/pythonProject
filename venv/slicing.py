#syntax for slicing - [start:end] , [start:end:step]
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
x2 = np.array([[1,2,3],[4,5,6]])
print(x[1:4], "This output for input - print(x[1:4]) this explains leave first number print till 4")
print(x[0:9:2],"This output for input - print(x[0:9:2] this explains leave 0th number print till 9 but 2nd number")
print(x[0:9:3],"This output for input - print(x[0:9:3] this explains leave 0th number print till 9 but 3rd number")
print(x[0:-2:1],"This output for input - print(x[0:-2:1] this explains leave 0th number print till 9 but '-' last 2 number")
print(x2[1:2,1] ,"This output for input - print(x2[1:2,1]) this prints 2 dim array 2nd number index number 1")
print(x2[0:2,1:4], "This output for input - print(x2[0:2,1:4] this prints both but leaves 1st index")