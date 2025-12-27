arr=list(map(int,input().split()))
zero=[x for x in arr if x==0]
one=[x for x in arr if x==1]
two=[x for x in arr if x==2]
print(zero+one+two)
