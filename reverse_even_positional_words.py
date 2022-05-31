n=input()
k=n.split()
for i in range(len(k)):
    if i%2==0:
        print(k[i][::-1],end=' ')
    else:
        print(k[i],end=' ')