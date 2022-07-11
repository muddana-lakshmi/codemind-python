n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    sum=sum+i
avg=sum//len(l)
if avg in l:
    print("True")
else:
    print("False")