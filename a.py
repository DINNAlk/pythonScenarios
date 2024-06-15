def u(ubetta):
    x=[]
    for i in ubetta:
        result=i%2
        if(result==0):
            x.append(i)
        else:
            continue
    return x

ubetta=[1,2,3,4,5,6,7,8,9,10]
y=u(ubetta)
print(y)
