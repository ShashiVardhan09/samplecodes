t=int(input())
t1=0
while t>0:
    n=int(input())
    cp=list(map(int,input().split()))
    c=0
    
    for i in range(0,len(cp)-2):

        if cp[i+1]>max(cp[i],cp[i+2]):
            c=+1
    t1+=1
    print('Case #'+str(t1)+': '+str(c))
    t-=1
        