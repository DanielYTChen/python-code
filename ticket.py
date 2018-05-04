def ticket(age):
    if age < 15:
        print("children")
    elif age < 65 :
        print("adults")
    else :
        print("seniors")

def ticket3(age):
    type="children" if age <15 else "adults" if age <65 else "seniors"
    print(type)
def test():
    ticket3(20)
    ticket3(40)
    ticket3(60)
test()