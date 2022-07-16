s=input()
z='AEIOUaeiou'
q='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
r=[]
x=0
for i in s:
    r.append(i)
#print(r)
for i in range(len(r)):
    if len(r)%2==0:
        if i<len(r)//2:
            if ((r[i] in z) and (r[len(r)-1-i] in q)) or ((r[i] in q) and (r[len(r)-1-i] in z)):
               x+=1
    else:
        if i<=len(r)//2:
            if ((r[i] in z) and (r[len(r)-1-i] in q)) or ((r[i] in q) and (r[len(r)-1-i] in z)):
                x+=1
print(x)