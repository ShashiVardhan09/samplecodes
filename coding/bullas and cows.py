s=input()
g=input()
s=list(s)
g=list(g)
A=0
B=0
x=len(s)
y=len(g)
i=0
while i<x:
    print(i)
    if s[i]==g[i]:
        print(i) 
        A+=1
    elif s[i]!=g[i]:
        if y>0:
            for j in range(0,y):                        
                if s[i]==g[j] and s[j]!=g[j]:
                    g[j]=-1
                    print(i)
                    print(y)
                    B+=1
                    print(s)
                    print(g)
                    break
    i+=1
print(str(A)+'A'+str(B)+'B')
