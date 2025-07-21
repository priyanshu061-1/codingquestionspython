def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k > n
    rotated = arr[-k:] + arr[:-k]
    return rotated

n, k = map(int, input().split())
arr = list(map(int, input().split()))
rotated_arr = rotate_array(arr, k)
print(*rotated_arr)
