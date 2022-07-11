n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    sum=sum+i
avg=sum/len(l)
print("{:.2f}".format(avg))