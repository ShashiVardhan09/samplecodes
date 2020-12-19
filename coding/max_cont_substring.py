t=int(input())
for t in range(1,t+1):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    i=0
    while i<n-1:
        j=i
        cd=l[i+1]-l[i]
        while j<n-1 and cd==l[j+1]-l[j]:
            j+=1
        c=max(c,j-i+1)
        i=max(i+1,j)
    print('Case #'+str(t)+':',c)
