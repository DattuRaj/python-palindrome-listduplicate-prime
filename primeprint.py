n=int(input('enter num for range to print prime nums'))

i=1
while i<=n:
    j=1           #j for nested loop
    cnt=0          #counting
    while j<=n:
        if i%j==0:
            cnt=cnt+1
        j=j+1
    if cnt==2:
        print(i,end=" ")
        
    i=i+1