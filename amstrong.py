def armstrong(n):
    original = n
    ans = 0
    while n:
        a = n % 10
        ans += a * a * a
        n = n // 10
    return ans == original

n = int(input("Enter the number: "))
if armstrong(n):
    print("Yes, it's an Armstrong number!")
else:
    print("Nope, not an Armstrong number.")
