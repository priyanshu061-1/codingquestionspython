def isvalid(s):
    star = 0
    hash_ = 0

    for ch in s:
        if ch == "*":
            star += 1
        elif ch == "#":
            hash_ += 1

    print(star - hash_)

s = "###**"
isvalid(s)
