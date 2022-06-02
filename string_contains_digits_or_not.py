n=int(input())
c=0
for i in range(0,n):
    k=input()
    k=k.lower()
    c=0
    for j in k:
        if j in '1234567890':
            c+=1
    if c>0:
        print("Yes")
    else:
        print("No")
    