import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
#sns.distplot([0, 1, 2, 3, 4, 9, 6], hist=True)
#sns.distplot([0, 1, 2, 3, 4, 5, 6], hist=false)
sns.distplot([random.normal(loc=5,scale=3,size=2)])
plt.show()