i=5
while(i>0):
    for j in range(i):
        print('*',end='')
    i-=1
    print('')
    
for i in range(1,6):
    for j in range(5-i+1):
        print('*',end='')
    print('')