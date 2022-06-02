n=input()
n=n.lower()
n=n.split()
c=0
for i in n:
    k=i[::-1]
    if i==k:
        c+=1
print(c)