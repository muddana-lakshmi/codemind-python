n=input()
n=n.split()
m=0
for i in n:
    if len(i)>m:
        m=len(i)
print(m)