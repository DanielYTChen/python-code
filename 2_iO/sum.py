import sys
def sum_lines():
    for line in sys.stdin:
        line = line.strip() #??
        print(line) 
        token = line.split() #??
        #print(token)
        #print(len(token))
        total=sum([float(token) for token in token])
        total=0
        for i in range(0,len(token)):
            total+=float(token[i])
        print(total)
sum_lines()