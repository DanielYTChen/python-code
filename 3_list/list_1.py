###印出 a 的第 3 個元素
#印出 a 的倒數第 1 個元素
#在 a 的最後新增一個數字 5 之後印出 a 的內容
#a[1] = 1 之後印出 a 的內容
#建立一個新的 list b, 內容為 a 的第 2 到第 3 個元素
#建立一個新的 list c, 內容為 a 的第 2 到最後一個元素
#建立一個新的 list d, 內容為 a 的第 1 到倒數第 2 個元素
#建立一個新的 list e, 內容為 a 的第 2 到倒數第 2 個元素
#建立一個新的 list f, 內容和 a 完全相同, 請驗證修改 f 不會修改到 a, 並想一想直接用等號將 f 指定為 a 有什麼不同?
#建立一個新的 list g, 內容為 a 原本的內容但最後加上 [10, 20] 例如: a 為 [3, 1, 4, 2, 5], 加上 [10, 20] 後變成 [3, 1, 4, 2, 5, 10, 20]將 a 中的從位置 2 到 3 的部份代換為 [7, 8, 9] 之後印出 a 的內容. 例如: a 為 [3, 1, 4, 2, 5], 代換後變成 [3, 1, 7, 8, 9, 5]###
a=[3,"1",4,2]
print(a[3],sep="\n")
print(a[-1],sep="\n")
a.append(5)
print(a,sep="\n")
a[1]=1
print(a,sep="\n")
b=a[2:4]
print(b)
c=a[2:]
print(c)
d=a[1:-1]
print(d)
e=a[2:-1]
print(e)
f=[]
for el in a:
    f.append(el)
f[0]=99
print(a,f,sep="\n")
g=a+[10,20]
print(g)
a[2:4]=[7,8,9]
print(a)