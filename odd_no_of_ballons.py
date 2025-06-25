def oddballon(e):
    b1=0
    g1=0
    r1=0
    y1=0

    for i in range(len(e)):
        if e[i]=="b":
            b1+=1

        elif e[i]=="y":
           y1+=1

        elif e[i]=="r":
            r1+=1

        else:
            g1+=1

    if b1%2 !=0:
        return "b"
    elif y1%2!=0:
        return "y"
    elif g1%2!=0:
        return "g"
    elif r1%2!=0:
        return "r"
    else:
        print("no odd ballons")

e=["b","b","r","r","y","y"]
r=oddballon(e)
print(r)