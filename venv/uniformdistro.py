#a - lower bound -0.0
#b - upper bound -1.0
#size - size of array
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
#x = random.uniform(size=(2,3))
#sns.distplot([random.normal(loc=5,scale=3,size=2)])
sns.distplot([random.uniform(size=(2,3))])
plt.show()
#print(x)