def sumcube(start,end):
    cubesum=0
    for i in range(start,end+1):
        cubesum+=i**3
    
    print(cubesum)

start=3
end=6
sumcube(start,end)
