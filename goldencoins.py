def find_rooms(N,K,coins):
    start,end,currentsum=0,0,0
    resultstart,resultend=0,float('inf')

    while currentsum<N:
        currentsum+=coins[end]

        while currentsum>K:
            currentsum-=coins[start]
            start+=1

        if currentsum==K:
            if end-start<resultend-resultstart:
                resultstart,resultend=start,end

        end+=1

    if resultend==float('inf'):
        return "no soln found"
    
    else:
        return resultstart+1,resultend+1