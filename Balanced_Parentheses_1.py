n=input()
c=0
s=0
d=0
e=0
j=0
k=0
for i in n:
    if i=='(':
        c+=1
    elif i==')':
        s+=1
    elif i=='{':
        d+=1
    elif i=='}':
        e+=1
    elif i=='[':
        j+=1
    elif i==']':
        k+=1
if (c==s) and (d==e) and (j==k):
    print("True")
else:
    print("False")