#finding duplicate items in list

cnt=0

l=[1,2,3,4,5,7,2,4,9,8,45,12,13,45,65,47,58,98,56,45] 

dupli=[]

for i in l:
    x=i  #storing l elements
    j=0
    cnt=0               #counting dupli element
    while j<len(l):
        if x==l[j]:
            cnt=cnt+1
            if (cnt>1) and (x not in dupli):
                dupli.append(x)             #adding duplicate values to dupli list
                print(l[j])
        j=j+1
        
print(dupli,end=" ")
        
        
        
        
    
       