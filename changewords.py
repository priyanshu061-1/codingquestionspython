def changewords(a, b):
    result_a = ""
    result_b = ""

    # Replace vowels in 'a' with '%'
    for ch in a:
        if ch in 'aeiouAEIOU':
            result_a += '%'
        else:
            result_a += ch

    # Replace 'b' or 'y' in 'b' with '#'
    for ch in b:
        if ch in 'byBY':
            result_b += '#'
        else:
            result_b += ch

    print("Modified a:", result_a)
    print("Modified b:", result_b)

# Taking input
a = input("Enter string a: ")
b = input("Enter string b: ")

changewords(a, b)
