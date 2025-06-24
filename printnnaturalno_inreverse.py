def printreverse(n):
    if n<=0:
        return 0 
    else:
        print(n)
        printreverse(n-1)
r= printreverse(20)
print(r)