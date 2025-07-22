def is_palindrome_sum(n):
    original_n = n
    digit_sum = 0

    # Step 1: Find the sum of digits
    while n > 0:
        digit_sum += n % 10
        n = n // 10

    # Step 2: Reverse the digit sum
    temp = digit_sum
    reversed_sum = 0
    while temp > 0:
        remainder = temp % 10
        reversed_sum = reversed_sum * 10 + remainder
        temp = temp // 10

    # Step 3: Check if digit sum is a palindrome
    return digit_sum == reversed_sum

# Example usage
n = int(input("Enter a number: "))
if is_palindrome_sum(n):
    print("Sum of digits is a palindrome.")
else:
    print("Sum of digits is NOT a palindrome.")