def f1(n,arr):
    itemcount=0

    for i in range(len(arr)):
        if(arr[i]>n):
            itemcount+=1

    
    print(itemcount)
n=5
arr=[0,1,2,3,4]
f1(n,arr)