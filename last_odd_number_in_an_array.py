n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1,-1,-1):
    if l[i]%2==1:
        print(l[i])
        break
