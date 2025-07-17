def selection(list1):
    for i in range(len(list1)):
        minindex=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[minindex]:
                minindex=j

        list1[i],list1[minindex]=list1[minindex],list1[i]

    print(list1)
selection([34,23,54,22,11,43,52])