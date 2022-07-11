n=input()
n=n.split()
m=99
for i in n:
    if len(i)<m:
        m=len(i)
print(m)