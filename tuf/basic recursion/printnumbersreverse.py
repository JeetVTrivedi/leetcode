def printreverse(i,n):
    if i<n:
        return
    print(i,end=' ')
    printreverse(i-1,n)
i=10
n=1
printreverse(i,n)