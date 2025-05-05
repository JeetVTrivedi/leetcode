n=5
for  i in range(n):
    for j in range(i+1):
        print(chr(65+(n-i+j-1)),end=' ')
    print('')