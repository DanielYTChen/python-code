from math import pi
pi  # 3.141592653589793
def squareList(nums):
   return[i ** 2 for i in nums]

def absList(nums, x):
   return[x for x in nums if abs(x)<x]
def piList(n):
   return[round(pi,i) for i in range(1,n+1)]