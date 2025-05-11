def printnumber(i,n):
    if i>n:
        return
    print(i,end=' ')
    
    printnumber(i+1,n)
i=1
n=10
printnumber(i,n)