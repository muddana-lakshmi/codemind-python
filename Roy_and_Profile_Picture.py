n=int(input())
k=int(input())
for i in range(0,k+1):
    w,h=map(int,input().split())
    if w>=n and h>=n:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")
    elif w<n or h<n:
        print("UPLOAD ANOTHER")