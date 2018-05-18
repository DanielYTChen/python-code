def result(ans, guess):
    A=0
    B=0
    for idxa,vala in enumerate(ans):
       for idxg,valg in enumerate(guess):
           if  vala == valg: 
               if idxa==idxg:
                  A+=1
               else:
                  B+=1
    return str(A)+"A"+str(B)+"B"

'''def emumList(arr):
    for idx,el in enumerate(arr):
        print(idx+1,". ",el,)
emumList(["apple","orange","banana"])'''


def result2(ans, guess):
    A=0
    B=0
    for idxa,vala in enumerate(ans):
       if ans[idxa]==guess[idxa]:
            A+=1
       elif vala in guess:
            B+=1
    return str(A)+"A"+str(B)+"B"
print(result('1234', '4321'))
print (result2('4657', '9658'))
print (result2('9876', '6879') )