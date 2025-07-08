def compression(s):
    if not s:
        return ""
    
    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1  # reset count for new character
    
    # Add the last group
    compressed += s[-1] + str(count)
    
    return compressed

s="aaabbcc"
f1=compression(s)
print(f1)