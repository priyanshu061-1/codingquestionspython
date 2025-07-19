def maxcount(arr):
    count=1
    max_so_far=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>max_so_far:
            count+=1

            max_so_far=arr[i]

    return count

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))
print("Max count:", maxcount(arr))