n=input()
n=n.split()
x=0
for i in n:
    k=list(i)
    for j in range(len(k)):
        if j==0:
            if k[j] in 'aeiouAEIOU':
                x+=1
print(x)
        