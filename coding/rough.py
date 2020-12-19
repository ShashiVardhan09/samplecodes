x=int(input())
h=int(input())
for l in range(x,h+1):
    chk=[2,3,5,7]
    for i in chk:
        c=0
        if l%i==0:
            c+=1
    if c>=1:
        pass
    else:
        if l<8:
            c=0
            for i in range(1,8):
                if l%i==0:
                    c+=1
            if c<=2:
                if l+6<=h and l+6<9:
                    c=0
                    for i in range(1,8):
                        if (l+6)%i==0:
                            c+=1
                    if c<=2:
                        print(l,l+6)
        if l+6<=h:
            c=0
            for i in chk:
                if (l+6)%i!=0:
                    c+=1
            if c==4:
                print(l,l+6)
        else:
            break
