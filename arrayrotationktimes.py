def arrayrotation(arr,k,indices):
    n=len(arr)

    def rotateonce(arr):
        lastelement=arr[-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=lastelement

    for j in range(k):
        rotateonce(arr)

    result=[arr[i] for i in indices]
    return result


arr=[1,3,4,5,6,4]
k=4
indices=[1,2,3]

f1=arrayrotation(arr,k,indices)
print(f1)

        

