a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
l1=set(l1)
l2=set(l2)
if l1==l2:
    print("True")
else:
    print("False")