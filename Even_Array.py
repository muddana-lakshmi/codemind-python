n=int(input())
l=list(map(int,input().split()))
x=0
for i in l:
    if i%2==1:
        x+=1
if x>0:
    print("False")
else:
    print("True")