def subarrays(arr, target):
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == target:
                print(arr[i:j+1])

arr = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7
subarrays(arr, target)
