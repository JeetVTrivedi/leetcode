def sumoffirstn(i,n,sum):
    if i>n:
        return sum
    sum+=i
    return sumoffirstn(i+1,n,sum)
sum=0
sum=sumoffirstn(1,5,sum)
print(sum)

