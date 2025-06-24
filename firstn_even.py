def firstneven(n):
    if n==0:
        return 0
    else:
        firstneven(n-1)
        print(2*n,end=' ' )

r=firstneven(30)
print(r)
