x=[2,3,4]
#i is element
for i in x:
    print(i,end=" ")
print()
#i is position
for i in range(len(x)):
    print(x[i],end=" ")
print()
# idx&value
for idx,i in enumerate(x):
    print(idx+1,i,sep=" : ")
print()

x.append(5)
print(x)

y=[1,2]
z=x+y
print(x,y,z,sep="\n")

z=x
z[0]=99
print(x,z,sep="\n")

x.append(y)
print(x)

print(x[len(x)-1])
print(x[-1])