n= 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    for a in range(n*2-i*2):
        print(' ',end='')
    for j in range(1,i+1):
        print(i-j+1,end='')
        
    print('')

#or 
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    for a in range(n*2-i*2):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    print(' ')    