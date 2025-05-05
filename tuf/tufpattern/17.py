n=4
for i in range(n):
    for a in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(chr(65+j),end='')
    for k in range(i,0,-1):
        print(chr(65+k-1),end='')
    for b in range(n-i-1):
        print(' ',end='')
    print('')