def fib(n):
    a,b=0,1
    for i in range(1,n):
        a,b=b,a+b
    return b
print(fib(3))
print(fib(5))
print(fib(9))
def fib2(n):
     a,b=0,1
     for i in range(1,n):
      c=a+b
      a=b
      b=c
     return b

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.show()