digit=0
newnum=0
x=1020304055000
while(x>0):
    digit=x%10
    newnum=newnum*10+digit
    
    x=x//10
print(newnum)