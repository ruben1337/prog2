import random
import math
import matplotlib.pyplot as plt

n = 1000
nc = 0
ns = 0
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    ns +=1
    if x**2+y**2<=1:
        nc+=1
        plt.plot(x,y,'ro')
    else:
        plt.plot(x,y,'bo')
print(nc)
pi = 4*nc/ns
print(pi)
print(math.pi)
plt.show()