def fun(x,y,n):
    arr[x-1]=y
    ans=1

    for i in range(1,n):
        if arr[i]=arr[i-1]:
            ans+=1
    return"number of students part of metricsare",ans

n=int(input("enter number of students"))
k=int(input("enter no of evaluations:"))

arr=[]

for i in range(n):
    arr.append(int(input("enter marks of student[i+1]:")))

for i in range(k):
    x=int(input("enter matrix position to be change"))
    y=int(input("enter revaluation marks"))

    