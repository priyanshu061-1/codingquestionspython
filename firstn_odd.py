def firstnodd(n):
    if n== 0:
        return 0
    else:
        firstnodd(n-1)
        print(2*n-1,end=' ')
r=firstnodd(9)
print(r)