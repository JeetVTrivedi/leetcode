n=4
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        left=j
        bottom=(2*n-1)-i-1
        right=(2*n-1)-j-1
        distance=min(top,left,bottom,right)
        print(4-distance,end='')
    print('')