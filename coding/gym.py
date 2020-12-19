t=int(input())
t1=0
while t>0:
    n,m=map(int,input().split()) #n= size of list , m= no of elements can be insterted in list
    l=list(map(int,input().split()))
    a=[]
    for x in range(0,len(l)-1):
    	ele=l[x]-l[x+1]
    	a.append(abs(ele))
    while m>0:
    	if max(a)%2==0:
    		p=a.index(max(a))
    		a.insert(p,int(max(a)/2))
    		a.insert(p+1,int(max(a)/2))
    		a.pop(p+2)

    	elif max(a)%2!=0:
    		p=a.index(max(a))
    		a.insert(p,int((max(a)+1)/2))
    		a.insert(p+1,int((max(a)-1)/2))
    		a.pop(p+2)
    	m-=1
    t1+=1
    print('Case #'+str(t1)+': '+str(max(a)))
    t-=1
