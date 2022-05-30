n=input()
k=input()
c=0
for i in n:
    if i==k:
        c+=1
if c==0:
    print("-1")
else:
    print(c)