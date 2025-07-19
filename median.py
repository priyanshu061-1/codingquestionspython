def median(arr,n):
    ans=0
    sum=0
    a=0
    if(n%2==0):

        for i in range(len(arr)):
             sum=sum+arr[i]
             ans=sum//n
    
    else:
        a=(n//2)
        ans=arr[a]

    return ans

arr=[20,30,40,50,60,70,80]
n=7
print(median(arr,n))