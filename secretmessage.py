def encrypt(s):
    ans=" "
    for i in s:
        if ord(i)<=ord('u'):
            ans+=chr(ord(i)+5)
        
        else:
            ans+=chr(ord(i)-ord('v')+ord('a'))

    print(ans)

s='hello'
encrypt(s)