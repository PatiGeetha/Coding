def find_minimum(a, b):
    # code here  
    list1=[]
    r1=a+b
    list1.append(r1)
    r2=a-b
    list1.append(r2)
    r3=a*b
    list1.append(r3)
    try:
        if b!=0:
            r4=a//b
            list1.append(r4)
    except:
        pass
    return min(list1)
