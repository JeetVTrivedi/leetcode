n=4
for i in range(1,n*2):
    if(i<=n):
        for j in range(i):
            print('*',end='')
        print('')
    else:
        for j in range(n*2-i):
            print('*',end='')
        print('')