def readn(n):
    product = 1
    while n > 0:
        t = n % 10
        product *= t
        n = n // 10
    print(product)

n = 32234
f1 = readn(n)
