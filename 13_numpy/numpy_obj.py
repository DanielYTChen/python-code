import numpy as np
import matplotlib.pyplot as plt 
arr = np.arange(10)
print(arr)
print(arr.ndim)
print(arr.shape)

arr2= np.arange(5,50,3)
print(arr2)
arr2_1=arr2**1.2
print(arr2_1)
arr3x=np.arange(10,50,3)
arr3y=arr3x*2+5
arr4x=np.linspace(0,10,21)
arr4y1=arr4x*2
arr4y2=arr4x*3
plt.plot(arr2,arr2_1,'--bo',arr3x,arr3y,'-rv')
plt.plot(arr4x,arr4y1,'--go',arr4x,arr4y2,'-yx')
plt.show()