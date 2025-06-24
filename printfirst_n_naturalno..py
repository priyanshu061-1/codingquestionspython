def printno(n):
    if n<=0:
        return 0
    else:
        printno(n-1)
        print(n)

r=printno(-1)
print(r)