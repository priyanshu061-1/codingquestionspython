secondeven = 0
secondodd = 0

# Fixing this line: input() just takes user input; no need to write 'list'
arr = list(map(int, input().split()))

odd = []
even = []

# You meant to separate odd and even numbers based on value, not index
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

odd = sorted(odd)
even = sorted(even)

# Use pop correctly to get the second largest
secondeven = even.pop(-2)
secondodd = odd.pop(-2)

print(secondeven + secondodd)
