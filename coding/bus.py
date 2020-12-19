d=int(input())
l=list(map(int,input().split()))
ls=[]
while d>0:
    for j in range(0,len(l)):
        if d%l[j]==0:
            ls[j].append(d)
   

    d-=1
print(ls[0])