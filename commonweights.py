def common(m,n,arr):

    cset=set(arr)
    updatedlist=[]
    for i in range(1,m+1):
        if i not in cset:
            updatedlist.append(i)

        
    return updatedlist

m=10
n=3
arr=[2,3,5]
print(common(m,n,arr))