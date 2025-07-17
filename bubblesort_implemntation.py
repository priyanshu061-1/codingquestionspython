def bubble(list1):
    for r in range(1,len(list1)):
        for i in range(len(list1)-r):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
    
    print(list1)

bubble([34,67,12,89,24,55])
