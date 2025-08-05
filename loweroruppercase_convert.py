def convert(s):
    uppercount = 0
    lowercount = 0

    for ch in s:
        if ord(ch) >= 65 and ord(ch) <= 90:
            uppercount += 1
        elif ord(ch) >= 97 and ord(ch) <= 122:
            lowercount += 1

    result = ""

    if uppercount > lowercount:
        for ch in s:
            if ord(ch) >= 97 and ord(ch) <= 122:
                result += chr(ord(ch) - 32)
            else:
                result += ch
    else:
        for ch in s:
            if ord(ch) >= 65 and ord(ch) <= 90:
                result += chr(ord(ch) + 32)
            else:
                result += ch

    return result

s = "HIhow"
print(convert(s))
