n = int(input())
m = int(input())

sum_divisible = 0
sum_not_divisible = 0

for i in range(1, m+1):
    if i % n == 0:
        sum_divisible += i
    else:
        sum_not_divisible += i

print(abs(sum_not_divisible - sum_divisible))