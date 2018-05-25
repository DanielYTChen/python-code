import sys
birthday={}
def test():
    for line in sys.stdin: #這裡不能用input，因為input裡面沒跟你說有幾行
        line=line.split()
        m=int(line[1])
        if birthday.get(m):
            birthday[m]+=1
        else:
            birthday[m]=1
    for i in range(1,13):
        print(i,birthday.get(i))

test()