n=input()
c=0
x=0
for i in n:
    c=0
    for j in n:
        if i==j:
            c+=1
    if c>1:
        x+=1
if x==0:
    print("True")
else:
    print("False")