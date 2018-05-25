snums={}
def prs(name):
    if snums.get(name):
        print(name,snums.get(name))
    else:
        print("陳韋安臭87")
def test():
    num=int(input())
    for i in range(0,num):
        line=input()
        tokens=line.split()
        for x in range(1,5):
          snums[tokens[0]+"-"+str(x)]=int(tokens[x]) #因為X是數字不能跟字串相加，所以加STR
    #print(snums)
    num=int(input())
    for i in range(0,num):
        line=input()
        prs(line)
test()
        
      
