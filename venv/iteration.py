import numpy as nd
x = nd.array([[[1,2,3,4,5,6,],[7,8,9,10,11,12],[13,14,15,16,17,18]]])
def normal_itr():
#print (x)
    for y in x:
    #print(y)
        for z in y:
       # print(z)
            for a in z:
   #         b = a.astype("S")
                print(a)
def fast_itr():
                a=input("type yes if you want normal\n")
                if a == "yes":
                  for arr in nd.nditer(x):
                    print(arr)
                else:
                        for arr in nd.nditer(x,flags=["buffered"],op_dtypes=['S']):
                            print(arr)
fast_itr()
def enum():
    for j in nd.ndenumerate(x):

        print(j)
print("which shows arrays or matrics shows which dimension specific number placed")
enum()
exit()