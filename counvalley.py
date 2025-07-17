def countvalleys(steps,path):
    sealevel=0
    valleys=0

    for step in path:
        if step=='U':
            sealevel+=1

        else:
            sealevel-=1

        if step=='U' and sealevel==0:
            valleys+=1

    return valleys

steps=8
path='UUDDDDUUDDUU'

f1=countvalleys(steps,path)
print(f1)