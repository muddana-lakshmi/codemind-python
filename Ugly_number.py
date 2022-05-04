n=int(input())
x=0
while n!=1:
    if n%5==0:
        n=n//5
    elif n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    else:
        print("Not Ugly Number")
        x+=1
        break
if x==0:
    print("Ugly Number")