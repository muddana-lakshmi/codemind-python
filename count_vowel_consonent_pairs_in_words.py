s=input()
l=list(s.split(' '))
z='AEIOUaeiou'
x=0
for i in range(len(l)):
    k=list(l[i])
    for j in range(len(k)):
        if len(k)%2==0:
            if j<len(k)//2:
                if ((k[j] in z) and (k[len(k)-1-j] not in z)) or ((k[j] not in z) and (k[len(k)-1-j] in z)):
                    x+=1
        else:
            if j<=len(k)//2:
                if ((k[j] in z) and (k[len(k)-1-j] not in z)) or ((k[j] not in z) and (k[len(k)-1-j] in z)):
                    x+=1
print(x)