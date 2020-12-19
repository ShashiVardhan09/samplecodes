t=int(input())
for t in range(1,t+1):
    n=int(input())
    l=list(map(int,input().split()))
    l1=[0]
    c=0
    for i in range(0,n-2):
        if (l[i]-l[i+1])==(l[i+1]-l[i+2]):
            c+=1
            l1.append(c)
        else:
            c=0
    if max(l1)>0:
        print('Case #'+str(t)+':',max(l1)+2)
    else:
        print('Case #'+str(t)+': 0')


