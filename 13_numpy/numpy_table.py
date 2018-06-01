import numpy as np 

def table(m,n):
    arr=[]
    for i in range(1,m+1):
        sub=[]
        for j in range(1,n+1):
            sub.append(i*j)
        arr.append(sub)
    return np.array(arr)
def table1(m,n):
    arr=[[i*j for j in range(1,n+1) for i in range(1,n+1)]]
    return np.array(arr)


def test():    
    nparr=table(3,9)
    print(nparr)
    print(nparr.ndim)
    print(nparr.shape)
    print(nparr*2)
test()