t=int(input())
for x in range(1,t+1):
    n,b=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    l=sorted(l)
    for i in l:
        if i<=b:
            b=b-i
            count=count+1
           
    print('Case #'+str(x)+':'+str(count))
 
        
    
     