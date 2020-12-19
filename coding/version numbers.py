v1=list(map(int,v1.split('.')))
v2=list(map(int,v2.split('.')))
print(v1)
if len(v1)>len(v2):
    x=len(v1)-len(v2)
    for i in range (x):
        v2.append(0)
elif len(v1)<len(v2):
    x=len(v2)-len(v1)
    for i in range (x):
        v2.append(0)
print(v2)
print(v1)
for i in range(0,len(v1)):
    if v1[i]>v2[i]:
        print('1')
        break
    elif v1[i]<v2[i]:
        print('-1')
        break
    elif v1[i]==v2[i] and i==len(v1)-1:
        print('0')





