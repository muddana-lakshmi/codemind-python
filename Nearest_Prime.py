t=int(input())
s=0
q=0
for k in range(t):
    n=int(input())
    for i in range(n+1,n*n):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            s=i
            break
    for i in range(n,0,-1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            q=i
            break
    if abs(s-n)<abs(q-n):
        print(s)
    elif abs(q-n)<abs(s-n):
        print(q)
    elif abs(s-n)==abs(q-n):
        print(q)