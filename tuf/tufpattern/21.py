n=4
for i in range(n):
    for j in range(n):
        if(i!=0 and i!=n-1):
            if(j==0 or j==n-1):
                print("*",end='')
            else:
                print(' ',end='')
        else:
            print("*",end='')
    print('')