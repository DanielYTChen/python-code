import numpy as np 
import matplotlib.pyplot as plt
mat1= np.zeros((3,4))
print(mat1)
print(mat1.ndim)
print(mat1.shape)

mat2 = np.ones((3,3))
mat2_2=mat2*2*mat2
mat3=np.matmul(mat2,mat2_2)
print(mat2)
print(mat2_2) #好像跟線性代數算法不太一樣
print(mat3)

mat4=np.eye(3) #單位矩陣1,0
mat5=np.random.randn(5,5)
print(mat5)