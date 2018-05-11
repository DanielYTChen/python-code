num=list(range(5,0,-1))
print(num)
num[2]=100
print(num)

a=[1,2,3]
total=0
for el in a :
    total+=el
total2=sum(a)
print(total,total2)
b=range(5,0,-1)
total3=sum(b)
print(total3)

'''strA="stone"
strA[0]="Y"
print(strA) 這裡是錯誤的 str 不能亂變動'''

strA="Stone"
strA=list(strA)
strA[0]="Y"
print(strA) 
print(','.join(strA))

'''試著使用 range() 函數建立以下 list:

list1 內容為 [0, 1, 2, 3, 4]
list2 內容為 [2, 3, 4, 5, 6]
list3 內容為 [1, 3, 5, 7, 9]
list4 內容為 [5, 4, 3, 2, 1] '''
list1=list(range(0,5,1))
print(list1)
list2=list(range(2,7,1))
print(list2)
list3=list(range(1,10,2))
print(list3)
list4=list(range(5,0,-1))
print(list4)