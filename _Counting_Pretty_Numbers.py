n=int(input())
for i in range(0,n):
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        d=i%10
        if d==2 or d==3 or d==9:
            c+=1
    print(c)