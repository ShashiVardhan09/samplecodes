alpha="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
l=alpha.split()

def ExcelColumnNumber(s):
    #code here
    
    l1=[]
    for i in range(0,len(s)):
        index = l.index(s[i],0,len(l)) 
        l1.append(index+1)
        
    x=0
    y=0
  
    while y<len(l1)-1:
        x=26*l1[y]+x
        
        y+=1
    print(x+l1[-1])
s=input()
ExcelColumnNumber(s)       
   