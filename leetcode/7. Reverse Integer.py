def reverse( x: int) -> int:
        
    digit=0
    newnum=0
    num=x
    if(num<0):
        mul=-1
    else:
        mul=1
    x=abs(x)
    while(x>0):
        digit=x%10
        newnum=newnum*10+digit
        
        x=x//10
    if newnum>2**31 -1:
        return 0
    else:
        return newnum*mul
print(reverse(-7654321))