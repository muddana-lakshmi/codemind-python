n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
if len(l)>=3:
    l.remove(max(l))
    l.remove(max(l))
    print(max(l))
else:
    print(max(l))
    