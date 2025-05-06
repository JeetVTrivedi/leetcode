def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    num=x
    revnum=0
    while(num>0):
        revnum=revnum*10+num%10
        num=num//10
    if(x==revnum):
        return True
    else:
        return False
print(isPalindrome(12321))