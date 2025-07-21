def unique(b):
    uniid=[]
    for i in range(len(b)):
        
        if b[i]!=b[i+1]:
            uniid.append(b[i])

    return uniid

b=[1,1,2,2,4,4]
print(unique(b))